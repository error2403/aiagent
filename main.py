import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# load .env file
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

# create ai API client
client = OpenAI(
	base_url="https://openrouter.ai/api/v1",
	api_key=api_key,
)

# parse arguments to get user prompt
parser = argparse.ArgumentParser(description="AiAgent")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

# create message list to hold previous context
messages = [
	{"role": "user", "content": args.user_prompt}
]

# send message to AI client
response = client.chat.completions.create(
	model = "openrouter/free",
	messages=messages,
)

# check that response usage is not None
if response.usage is None:
	raise RuntimeError
	exit(1)

# print response info
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)

def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
