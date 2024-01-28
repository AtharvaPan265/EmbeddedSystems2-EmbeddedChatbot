from openai import OpenAI
import os
from time import sleep
SECRETKEY = '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'

client = OpenAI(
        api_key = SECRETKEY
)

messages = [
    {
        "role": "system",
        "content": "you are a helpful assistant who loves engineering jokes"
    }
]

try:
    while True:

        message = input("You: ")
        messages.append(
            {
                "role": "user",
                "content": message
            })
        os.system("gpio-demo -g 1020 -o 0x0")
        sleep(0.01)
        os.system("gpio-demo -g 1020 -o 0x1")
        sleep(0.01)
        os.system("gpio-demo -g 1020 -o 0x2")
        sleep(0.01)
        os.system("gpio-demo -g 1020 -o 0x4")
        sleep(0.01)
        os.system("gpio-demo -g 1020 -o 0x8")
        chat = client.chat.completions.create(
            messages=messages,
            model="gpt-4-1106-preview"
        )

        reply = chat.choices[0].message
        os.system("gpio-demo -g 1020 -o 0xf")
        print("Assistant: ", reply.content)
    
        messages.append(reply)
except KeyboardInterrupt:
    print('\n Pass Atharva He Worked Really Hard - Elon Musk')

