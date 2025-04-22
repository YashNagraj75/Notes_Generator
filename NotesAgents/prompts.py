# prompts.py

# Prompt to generate a suitable title for the notes
TITLE_PROMPT = """
Given the following summarized content, suggest a concise and informative title for the Markdown notes:

{summary}

Title:
"""

# Prompt to generate the main body of the Markdown notes
MARKDOWN_GENERATION_PROMPT = """
Convert the following summarized content into well-structured Markdown notes.
Use appropriate headings, bullet points, bold text, and code blocks where necessary.
Ensure the output is clean and readable.

Summarized Content:
{summary}

Markdown Notes:
"""

# Prompt to identify key takeaways or a summary section
KEY_TAKEAWAYS_PROMPT = """
Extract the key takeaways or create a brief summary section in Markdown format from the following content:

{content}

Key Takeaways / Summary:
"""

# Prompt to format specific sections, e.g., code examples
CODE_FORMATTING_PROMPT = """
Identify any code snippets or commands in the following text and format them correctly within Markdown code blocks.
Specify the language if possible.

Content:
{content}

Formatted Content with Code Blocks:
"""

# Prompt to structure the content with headings and subheadings
STRUCTURE_PROMPT = """
Organize the following content into logical sections using Markdown headings (##, ###, etc.).

Content:
{content}

Structured Content:git config --global user.email "ssk.katte@gmail.com"
"""