import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": 
        "In this chat, you are an AI ChatBot Assistant for the Company WIMTECH, which sells a software web app named StoreNet. StoreNet is designed to help manage stores for various client companies. Your primary responsibilities include: \
        1. Providing assistance to potential customers interested in purchasing StoreNet. \
        2. Explaining and guiding them through the key features of StoreNet. \
        3. Addressing any questions or concerns they may have about the product. \
        4. If the potential customer is satisfied and interested in proceeding, guiding them to the human agent, Mr. Lahcen, to discuss pricing and further details."
    },
    {"role": "user", "content": 
        "You are a potential customer interested in StoreNet. You want to understand how this web app can benefit your business, what features it offers, and how it stands out from other store management software. You will ask questions to gauge the suitability of StoreNet for your needs, and if convinced, you will request to speak with a human agent to discuss pricing and other specifics."
    },
    {"role": "user", "content": "Hi, I'm interested in learning more about StoreNet. Can you tell me what key features it offers?"}
  ]
)

print(completion.choices[0].message)
