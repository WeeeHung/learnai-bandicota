# Bandicota.ai

Powered by LLM (Large Language Model), our app serves as your vigilant guardian, analyzing text for potential scam indicators. 
Beyond detection, we are committed to educating and empowering users to recognize and combat scams effectively. 
Join us in the fight against fraudulent schemes and stay one step ahead in safeguarding your online presence.


## Setup

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/WeeeHung/learnai-bandicota.git
   ```
2. Navigate to the project directory:
   ```
   cd learnai-bandicota
   ```
3. Create a virtual environment:
   ```
   python -m venv .venv

    # Windows command prompt
    .venv\Scripts\activate.bat

    # Windows PowerShell
    .venv\Scripts\Activate.ps1

    # macOS and Linux
    source .venv/bin/activate
   ```
4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Run the app:
    ```
    streamlit run app.py
    ```

## Features

- Scam Detection and Analysis
- Scam Education (Generated Quiz)

## Codebase Description

This project is organized as follows:

- **`component/`**: Contains the features built for the webapp, such as the scam detection and scam education features.
    - **`homefeature.py`**: Contains the introduction and information on why scam detection and scam education are important.
    - **`mainfeature.py`**: Contains the scam detection feature. It provides the frontend layout using Streamlit and does text analysis using the llm.scamanalyzer module.
    - **`subfeature.py`**: Contains the scam education feature. It provides the frontend layout using Streamlit and generates questions based on email or text extracts using the llm.textgenerator module.
- **`llm/`**: Contains helper functions that make OpenAI API calls and perform operations using GPT-3.5 Turbo, such as text generation and text analysis.
    - **`scamanalyzer.py`**: Does parsing and analysis of text for scam indicators. Contains System and User Prompts required for the analysis.
    - **`textgenerator.py`**: Does text generation for scam education. Contains context and format for the email or text extract and the question. Contains System and User Prompts required for the generation.
    - **`client.py`**: Contains the OpenAI API client used to make API calls.
- **`.streamlit/secrets.toml`**: Contains the OpenAI API key used to make API calls. (git ignored as it contains sensitive information) 
- **`app.py`**: The main file that runs the web application.
- **`logo1.png`**: The logo used for the webapp.

Other files include:
- **`README.md`**: Contains the information about the project.
- **`requirements.txt`**: Contains the required dependencies for the project.


### Main Technologies Used

- **`Python`**: The primary language used in this project.
- **`Streamlit`**: The web framework used to build the webapp.
- **`OpenAI`**: The API used to generate the scam detection and scam education features.

## Usage

### Scam Detection and Analysis

1. Enter the text you want to analyze in the text box.
2. Click the "Check for Scam" button.
3. The app will return the scam analysis and the scam indicators found in the text.

### Scam Education

1. Click the "Generate Question" button.
2. The app will generate an email or text extract and a question based on the extract.
3. Answer the question and click the "Submit your answer" button.
4. The app will return the correct answer and an explanation.
5. Click the "Another Question" button to go back to step 2.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request