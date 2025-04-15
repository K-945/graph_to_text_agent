from openai import OpenAI

def chatgpt_api(user_prompt):
    client = OpenAI(
        base_url="",
        api_key=""
    )

    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0613",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
      ]
    )
    return response

def get_content(response):
    return response.choices[0].message.content



