import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

message1 = "I'm a beginner runner and I want to start training for a marathon. Can you help me?"


def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "open-mistral-7b"

    client = MistralClient(api_key=api_key)

    for chunk in client.chat_stream(
        model=model,
        messages=[
            ChatMessage(
                role="user",
                content="I'm a beginner runner and I want to start training for a marathon. Can you help me?",
            )
        ],
    ):
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


if __name__ == "__main__":
    main()
