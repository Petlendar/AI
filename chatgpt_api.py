from openai import OpenAI

client = OpenAI(
    api_key="" #api키 필요
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지에는 무엇이 있나요?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "",#이미지 경로 
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

#print(response.choices[0])
print(response) #총 토큰 개수 출력