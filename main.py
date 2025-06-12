import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

# Load your Hugging Face token from environment variables
token = os.getenv("HF_TOKEN")

if not token:
    st.error("HF_TOKEN is missing. Set it in your environment variables.")
    st.stop()

# Initialize the Hugging Face client
try:
    client = InferenceClient(token=token)
except Exception as e:
    st.error(f"Failed to initialize Hugging Face client: {e}")
    st.stop()

def generate(blog_title, keywords, num_words):
    try:
        # Generate a prompt for the blog post
        prompt = f"""Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog post should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."""

        # Use the client to generate the blog post
        completion = client.chat_completion(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[{"role": "user", "content": prompt}]
        )

        return completion.choices[0].message.content

    except Exception as e:
        st.error(f"An error occurred during blog generation: {e}")
        return None

st.set_page_config(page_title="BlogifyAI")
st.title("BlogifyAI: Your AI Writing Assistant")
st.subheader("An Application that can help users to craft perfect blogs")

with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog that You want to generate")
    blog_title = st.text_input("Enter Blog Title")
    keywords = st.text_area("Keywords (comma separated)")
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=250)
    submit_button = st.button("Generate Blog")

if submit_button:
    with st.spinner('Generating your blog...'):
        blog_content = generate(blog_title, keywords, num_words)
        if blog_content:
            st.write(blog_content)
