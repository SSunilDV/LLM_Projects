# YouTube Notes Generator

## Overview

YouTube Notes Generator is a web application that extracts the transcript from a YouTube video and generates comprehensive notes using Google's **Gemini-Pro (LLM)**. This helps users quickly review key points, decide whether to watch a video, and identify tools mentioned in the content.

## Features

✅ Extracts transcripts from YouTube videos using **YouTube Transcript API**\
✅ Uses **Google’s Gemini-Pro LLM** to generate detailed notes\
✅ Provides key takeaways and tools mentioned (free/paid)\
✅ Accepts additional queries for customized note generation\
✅ Displays the **YouTube video thumbnail** for quick reference\
✅ Built with **Streamlit** for an intuitive UI

## How It Works

1. **Enter the YouTube video link** 📌
2. Click **Generate Notes** 📝
3. Get **detailed notes & insights** instantly! ⏳

## Tech Stack

- **Python** 🐍
- **Streamlit** (UI Framework) 💻
- **Google Gemini-Pro (LLM)** 🤖
- **YouTube Transcript API** 🎥
- **dotenv** (for managing API keys) 🔑

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SSunilDV/LLM_Projects
   cd Youtube_Notes_Generator
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your API key:
   - Create a `.env` file in the root directory
   - Add your API key inside it:
     ```plaintext
     API_KEY=your_google_gemini_api_key
     (You can get Your Api key from Google Ai Studio.)
     ```
5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

- **Basic Notes Generation:** Enter a YouTube link and click "Generate Notes."
- **Customized Notes:** Provide an additional query to refine the notes based on your needs.

## Example Output

```
Key Takeaways from Video:
1. Introduction to AI-powered video summarization.
2. Discussion on tools like ChatGPT, Gemini, and Streamlit.
3. How to integrate AI in daily learning.

Tools Mentioned:
- ChatGPT (Free/Paid)
- Gemini AI (Free/Paid)
- Streamlit (Free)
```

## Future Enhancements

- 🛠️ Support for multiple languages 🌍
- 📌 Option to save & export notes 📄
- 🔍 AI-powered keyword extraction 🔑

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

MIT License

## Contact

For questions or feedback, reach out via LinkedIn or GitHub.

🚀 **Save time, learn smarter, and make informed decisions with YouTube Notes Generator!**

