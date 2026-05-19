#  BlogifyAI — Your AI Writing Assistant

BlogifyAI is a **Streamlit-based web application** that leverages Meta's **Llama 3.1 8B Instruct** model (via Hugging Face) to automatically generate comprehensive, engaging blog posts. Simply provide a title, keywords, and desired word count — and let the AI do the writing.

---

##  Features

-  **AI-Powered Blog Generation** — Uses Meta's `Llama-3.1-8B-Instruct` model via Hugging Face Inference API
-  **Customizable Output** — Control blog length (250–1000 words) and focus via keywords
-  **Simple Sidebar UI** — Clean, intuitive interface powered by Streamlit
-  **Secure Token Management** — API credentials managed through environment variables
-  **Real-time Generation** — Live spinner feedback while content is being generated

---

##  Tech Stack

| Technology | Purpose |
|---|---|
| [Python](https://python.org) | Core language |
| [Streamlit](https://streamlit.io) | Web UI framework |
| [Hugging Face Hub](https://huggingface.co) | LLM Inference API |
| [Meta Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | Language model |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

##  Project Structure

```
Blogify/
├── .devcontainer/        # Dev container configuration
├── .streamlit/           # Streamlit configuration
├── main.py               # Main application file
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

---

##  Getting Started

### Prerequisites

- Python 3.8+
- A [Hugging Face](https://huggingface.co) account with an API token
- Access to `meta-llama/Llama-3.1-8B-Instruct` (may require model access request)

### 1. Clone the Repository

```bash
git clone https://github.com/shivamvishwakarma25/Blogify.git
cd Blogify
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
HF_TOKEN=your_huggingface_api_token_here
```

>  Get your token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 4. Run the App

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

---

##  How to Use

1. Open the app in your browser.
2. In the **sidebar**, fill in:
   - **Blog Title** — The topic or headline of your blog post
   - **Keywords** — Comma-separated keywords to include
   - **Number of Words** — Slider from 250 to 1000 words
3. Click **"Generate Blog"**.
4. Your AI-generated blog post will appear on the main page.

---

##  Configuration

The app reads configuration from environment variables. You can also configure Streamlit settings via the `.streamlit/` directory (e.g., theme, server settings).

| Variable | Description | Required |
|---|---|---|
| `HF_TOKEN` | Hugging Face API token | ✅ Yes |

---

##  Key Dependencies

```
streamlit==1.45.1
huggingface_hub
python-dotenv==1.1.0
```

See [`requirements.txt`](./requirements.txt) for the full list.

---

##  Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

##  License

This project is open source. Please check the repository for license details.

---

##  Author

**Shivam Vishwakarma**
- GitHub: [@shivamvishwakarma25](https://github.com/shivamvishwakarma25)

---

>  **Note:** This app requires a valid Hugging Face token and access to the `meta-llama/Llama-3.1-8B-Instruct` model. Make sure you have the necessary permissions on Hugging Face before running the app.
