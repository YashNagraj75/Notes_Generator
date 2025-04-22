import os

from agents import (
    Agent,
    ModelSettings,
    OpenAIChatCompletionsModel,
    Runner,
    handoff,
    set_default_openai_api,
    set_default_openai_client,
)
from openai import AsyncOpenAI
from openai.types.responses import tool

from tools import get_ppt_content, get_video_transcript

set_default_openai_api("chat_completions")
client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)


NotesGenerator = Agent(
    name="Slide Layout Planner",
    model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client),
    model_settings=ModelSettings(temperature=0.9, tool_choice="required"),
    tools=[get_ppt_content, get_video_transcript],
)


async def main():
    notes = await Runner.run(
        NotesGenerator,
        "Make comprehensive notes for the content given",
    )
    print(notes.final_output)
    return notes.final_output
