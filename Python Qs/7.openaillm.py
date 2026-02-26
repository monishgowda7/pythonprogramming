key  =""

# this is a fake key, you should replace it with your own key from OpenAI. You can get it from https://platform.openai.com/account/api-keys

from openai import OpenAI
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
        {
            "role": "user",
            "content": "what is 2+2 ",
            
            # content will be prompt that will send to model and model will generate the response based on the prompt and return it to us.like chatgpt,gemini 
        }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


for choice in response.choices:
    print(choice.message.content)
