import subprocess
import os
from groq import Groq
client = Groq(api_key= os.environ.get("GROQ_API_KEY"))

def extract_audio_ffmpeg(input_video, output_audio):
    command = [
        "ffmpeg", "-i", input_video,
        "-vn",  # Disable video recording
        "-acodec", "libmp3lame",  # Audio codec
        "-q:a", "0",  # Audio quality
        output_audio
    ]
    subprocess.run(command, check=True)



def get_video_transcript():
    extract_audio_ffmpeg("/home/sujith27/llm_hackathon/Notes_Generator/assets/yt1z.net - Transformer Explainer- Learn About Transformer With Visualization (360p).mp4", "output_audio.wav")
    filename = os.path.dirname(__file__) + "/output_audio.wav"
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
        )
        print(transcription.text)
        