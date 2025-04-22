import os
import subprocess

from agents import function_tool
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def extract_audio_ffmpeg(input_video, output_audio):
    command = [
        "ffmpeg",
        "-i",
        input_video,
        "-vn",  # Disable video recording
        "-acodec",
        "libmp3lame",  # Audio codec
        "-q:a",
        "0",  # Audio quality
        output_audio,
    ]
    subprocess.run(command, check=True)


@function_tool
def get_video_transcript(path):
    extract_audio_ffmpeg(path, "output_audio.wav")
    filename = os.path.dirname(__file__) + "/output_audio.wav"
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
        print(transcription.text)
