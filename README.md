# AI News Generator

An AI-powered news generation application built using **Streamlit**, **CrewAI**, and **Cohere's Command R7B**. This tool allows users to create comprehensive blog posts or news articles about any topic by leveraging AI agents for research and writing.

## Features
- Multilingual support with seamless translation.
- Customizable content settings (e.g., topic, temperature).
- Outputs well-structured markdown files.
- Utilizes AI agents for research and content creation.

---

## How It Works
1. **Input Topic**: Enter the desired topic in the text area.
2. **Select Language**: Choose the output language from options like English, Spanish, French, German, or Chinese.
3. **Adjust Settings**: Fine-tune the temperature slider for creativity in writing.
4. **Generate Content**: Click the "Generate Content" button to create an article.
5. **Download**: Save the generated content as a markdown file.

---

## Prerequisites
- Python 3.8 or later
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/joggyjagz7/ai-news-generator.git
   cd ai-news-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add your API keys:
     ```
     API_KEY=your_api_key_here
     ```

---

## Running the Application
1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser:
   ```
   http://localhost:8501
   ```

---

## Folder Structure
```
ai-news-generator/
├── app.py                # Main application script
├── requirements.txt      # Dependencies for the project
├── README.md             # Project documentation
├── .env                  # Environment variables (API keys)
```

---

## Key Components
### AI Agents
1. **Senior News Correspondent**: Conducts thorough research and compiles an accurate news report with citations.
2. **Technical Copywriter**: Transforms the research into an engaging blog post, making technical content accessible.

### Tools
- **CrewAI**: Manages AI agents for research and writing tasks.
- **Google Translate**: Provides multilingual support.
- **Streamlit**: Creates the interactive user interface.

---

## Contributions
Contributions are welcome! Please submit a pull request or create an issue to report bugs or suggest features.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or support, reach out to [Ejiro](mailto:onose75@gmail.com).
