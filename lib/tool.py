import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

model = "gpt-4"

def get_completion(prompt):
    openai = get_openai()

    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

def get_openai():
    openai = OpenAI(
        api_key=get_openai_key(True),
        base_url=get_openai_url(True),
    )

    return openai

def get_openai_key(isProxy: bool = False):
    _ = load_dotenv(find_dotenv())

    key = 'OPENAI_API_KEY'
    if isProxy:
        key = 'OPENAI_API_KEY_PROXY'

    return os.environ[key]


def get_openai_url(isProxy: bool = False):
    _ = load_dotenv(find_dotenv())

    key = 'OPENAI_API_URL'
    if isProxy:
        key = 'OPENAI_API_URL_PROXY'

    return os.environ[key]

