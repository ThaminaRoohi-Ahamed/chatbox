from openai import OpenAI 

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
#A function
def token(messages):  
    for token in client.chat.completions.create(
     model="qwen/qvq-72b-preview",
        messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": messages
            },
            
            
        ]
        }
    ],
    stream=True
    

    ):
        print(token.choices[0].delta.content,end='')#print the data from 0th index

        