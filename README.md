# Lecture Notes Generator

An AI-powered system that automatically generates comprehensive lecture notes by combining information from educational videos and PowerPoint presentations. The system transcribes video content, extracts and structures information from slides, and enhances the notes with relevant imagery.


## Features

- **Video Transcription**: Accurately converts lecture speech to text using Groq's Whisper model
- **PowerPoint Analysis**: Extracts and structures content from PowerPoint slides
- **Content Integration**: Combines video transcripts and slide content into cohesive notes
- **Visual Enhancement**: Enriches notes with relevant images using Google Custom Search
- **User-Friendly Interface**: Simple Streamlit web app for easy file uploads and note generation

## System Requirements

- Python 3.13+
- FFmpeg (for audio extraction)
- API keys for:
  - Groq (transcription and text processing)
  - Google Cloud (for image search and Gemini model)
  - Google Custom Search Engine ID

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Notes_Generator.git
   cd Notes_Generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export GROQ_API_KEY="your_groq_api_key"
   export GEMINI_API_KEY="your_gemini_api_key"
   export CSE_ID="your_google_custom_search_engine_id"
   ```

## Usage

### Running the Web Interface

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Navigate to the provided URL (typically http://localhost:8501)

3. Upload your lecture materials:
   - Select a PowerPoint file (.ppt or .pptx)
   - Select a video file (.mp4, .avi, .mov, or .mkv)

4. Click "Generate Notes" and wait for processing to complete

5. View and download your generated lecture notes

### Using the API Programmatically

You can also generate notes programmatically by importing the main function:

```python
from notes_agents import main
import asyncio

# Generate notes from specific files
ppt_path = "path/to/presentation.pptx"
video_path = "path/to/lecture.mp4"

# Run the notes generation
notes = asyncio.run(main(ppt_path, video_path))

# Use the generated notes
print(notes)
# or save to file
with open("lecture_notes.md", "w") as f:
    f.write(notes)
```

## Pipeline Architecture

The system processes content through the following pipeline:

1. **File Upload**: PowerPoint and video files are uploaded through the web interface
2. **Parallel Processing**:
   - Video is processed for audio extraction and transcription
   - PowerPoint is processed for structured content extraction
3. **Content Integration**: Information from both sources is combined
4. **Image Enhancement**: Relevant images are searched and added to notes
5. **Notes Generation**: Final Markdown-formatted notes are generated
6. **Presentation**: Notes are displayed in the web interface

## Customization

You can customize the note generation process by modifying the prompts in `prompts.py`. The main notes generation prompt (Notes_Prompt) controls:

- Content structure and organization
- The balance between video and slide content
- Image search behavior
- Formatting and presentation style

## API Services Used

- **Groq API**: Used for high-quality audio transcription (Whisper model) and text structuring (LLama3)
- **Google Gemini API**: Used for image description and content synthesis
- **Google Custom Search**: Used for finding relevant images to enhance notes

## Troubleshooting

- If you encounter audio extraction issues, ensure FFmpeg is properly installed
- For transcription errors, check your Groq API key and connection
- For image search failures, verify your Google API keys and CSE ID
- If the application seems slow, consider processing shorter videos or presentations with fewer slides


## Acknowledgments

- Groq for providing the transcription and LLM APIs
- Google for Gemini API and Custom Search functionality
- The open-source community for tools like python-pptx and FFmpeg
