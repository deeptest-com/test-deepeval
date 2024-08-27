import os
from openai import OpenAI
from deepeval.models.base_model import DeepEvalBaseLLM
from lib.tool import get_openai_key, get_openai_url, get_openai

model = "gpt-4"

class OpenAIProxy(DeepEvalBaseLLM):
    def __init__(self, model):
        self.model = model

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()

        messages = [{"role": "user", "content": prompt}]
        response = chat_model.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message.content

    async def a_generate(self, prompt: str) -> str:
        chat_model = self.load_model()

        messages = [{"role": "user", "content": prompt}]
        response = chat_model.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message.content

    def get_model_name(self):
        return "Custom OpenAI Model Using Proxy"

def get_custom_model():
    openai = get_openai()
    custom_model = OpenAIProxy(model=openai)

    return custom_model

print(get_custom_model().generate("给我讲个中文笑话"))