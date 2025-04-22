import os

from agents import (
    Agent,
    ModelSettings,
    OpenAIChatCompletionsModel,
    Runner,
    handoff,
    set_default_openai_api,
    set_default_openai_client,
    FunctionTool,
    function_tool,
)
import asyncio
from openai import AsyncOpenAI
from prompts import Notes_Prompt
from tools import (
    get_video_transcript,
    generate_structured_output,
    get_image_description,
)


set_default_openai_api("chat_completions")
client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)


async def main(ppt_path, video_path):
    generate_structured_output_tool = FunctionTool(
        name="generate_structured_output",
        description="Parses a PowerPoint file and returns structured content.",
        params_json_schema={
            "type": "object",
            "properties": {
                "ppt_path": {
                    "type": "string",
                    "description": "The file path to the PowerPoint presentation.",
                }
            },
            "required": ["ppt_path"],
        },
        on_invoke_tool=lambda ctx, args_json: generate_structured_output(ppt_path),
    )

    # Define the FunctionTool for getting video transcript
    get_video_transcript_tool = FunctionTool(
        name="get_video_transcript",
        description="Transcribes a video file and returns the transcript.",
        params_json_schema={
            "type": "object",
            "properties": {
                "video_path": {
                    "type": "string",
                    "description": "The file path to the video.",
                }
            },
            "required": ["video_path"],
        },
        on_invoke_tool=lambda ctx, args_json: get_video_transcript(video_path),
    )

    # get_image_description_tool = FunctionTool(
    #    name="get_image_description",
    #    description="Searches the web for images based on a query and returns relevant image URLs and descriptions.",
    #    params_json_schema={
    #        "type": "object",
    #        "properties": {
    #            "query": {
    #                "type": "string",
    #                "description": "The search query for the image.",
    #            },
    #            "num_images": {
    #                "type": "integer",
    #                "description": "Number of images to fetch.",
    #            },
    #        },
    #        "required": ["query", "num_images"],
    #    },
    #    on_invoke_tool=lambda ctx, args_json: get_image_description(
    #        args_json["query"], args_json["num_images"]
    #    ),
    # )

    NotesGenerator = Agent(
        name="Notes Generator",
        model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client),
        model_settings=ModelSettings(temperature=0.9, tool_choice="required"),
        instructions=Notes_Prompt,
        tools=[
            generate_structured_output_tool,
            get_video_transcript_tool,
            get_image_description,
        ],
    )
    notes = await Runner.run(
        NotesGenerator,
        "Make comprehensive notes for the ppt and video lecture. using image search and make it visually appealing.",
    )
    print(notes.final_output)
    return notes.final_output


# if __name__ == "__main__":
#    ppt_path = "/home/yash/code/Notes_Generator/assets/Finetuning.pptx"
#    video_path = "/home/yash/code/Notes_Generator/assets/qlora.mp4"
#    asyncio.run(main(ppt_path, video_path))
#
