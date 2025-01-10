from openai import OpenAI


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def token(question):
    for token in client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": question
            },
            
            
        ]
        }
    ],
    stream=True


    ):


        print(token.choices[0].delta.content,end='')