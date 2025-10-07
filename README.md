

Markdown

# AI Resume & Portfolio Builder 🤖

This is a web application built with Python and Streamlit that uses the Google Gemini API to generate professional resumes and cover letters. Users input their details, and the AI crafts a professional summary, optimized work experience, and a tailored cover letter. The final resume can be downloaded as a styled `.docx` file.



## ✨ Features

* **Single-Call AI Generation**: Efficiently generates a summary, optimized experience, and cover letter in a single API call to avoid rate-limiting issues.
* **Multiple Resume Templates**: Choose between different professional styles, including a modern two-column layout.
* **Session-Based History**: A sidebar displays a history of all resumes generated during the current session for easy reference.
* **Styled Document Output**: Creates a professional, template-based resume that can be downloaded as a `.docx` file.
* **Interactive Web Interface**: An easy-to-use interface built with Streamlit.
* **Secure API Key Management**: Uses a `.env` file to keep your API key safe and out of the source code.

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **AI Model**: Google Gemini API (`google-generative-ai`)
* **Document Generation**: `python-docx`
* **Environment Variables**: `python-dotenv`

## 🚀 Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

* Python 3.8 or higher
* A Google Gemini API Key. You can get one for free from [Google AI Studio](https://aistudio.google.com/).

### 2. Create a `requirements.txt` file

Create a file named `requirements.txt` in your project folder and add the following lines to it:

```txt
streamlit
google-generative-ai
python-docx
python-dotenv
3. Installation Steps
Clone the repository (or set up your project folder):

Bash

git clone [https://github.com/your-username/ai-resume-builder.git](https://github.com/your-username/ai-resume-builder.git)
cd ai-resume-builder
Create and activate a virtual environment:

This keeps your project's dependencies isolated.

Bash

# Create the virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\Activate

# Activate on macOS/Linux
source venv/bin/activate
Install the required libraries:

Bash

pip install -r requirements.txt
Create a .env file:

Create a file named .env in the root of your project folder.

Add your Google Gemini API key to this file:

Code snippet

GEMINI_API_KEY="your_actual_api_key_paste_it_here"
4. Running the Application
With your virtual environment active, run the following command in your terminal:

Bash

streamlit run app.py
Your web browser should automatically open with the application running.

usage
Launch the application using the command above.

Fill in all the fields in the user interface (Name, Email, Skills, Experience, etc.).

Click the "Generate and Optimize Documents" button.

Review the AI-generated content in the expander boxes and the text area.

Click the "Download Resume as .docx" button to save your formatted resume.

📁 File Structure
.
├── app.py              # Main Streamlit application file (UI)
├── ai_logic.py         # Handles all AI prompt engineering and API calls
├── doc_generator.py      # Generates the styled .docx resume
├── .env                # Stores the API key (Do not commit to Git)
├── .gitignore          # Tells Git which files to ignore
└── requirements.txt      # Lists all project dependencies
📄 License
This project is licensed under the MIT License.