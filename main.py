import streamlit as st
import os
from pathlib import Path
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

def generate(blog_title, keywords, num_words):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemma-3n-e4b-it"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog post should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
    ):
        if chunk.text:  # Check if chunk.text is not None
            response_text += chunk.text
    return response_text


st.set_page_config(page_title="BlogifyAI")
st.title("BlogifyAI: Your AI Writing Assistant")
st.subheader("An Application that can help users to craft perfect blogs")

with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog that You want to generate")
    blog_title = st.text_input("Enter Blog Title")
    keywords = st.text_area("Keywords(comma separated)")
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=250)
    submit_button = st.button("Generate Blog")

if submit_button:
    with st.spinner('Generating your blog...'):
        blog_content = generate(blog_title, keywords, num_words)
        st.write(blog_content)
