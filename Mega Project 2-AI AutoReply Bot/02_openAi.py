from openai import OpenAI
# extra code file. helps to give example of openai. not connected with main code file or project
 
# pip install openai 

# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[20:30, 12/6/2024] Dibbo: jo sunke coding ho sake?
[20:30, 12/6/2024] Riyan: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Riyan: ye
[20:30, 12/6/2024] Riyan: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Dibbo: This is hindi
[20:31, 12/6/2024] Dibbo: send me some english songs
[20:31, 12/6/2024] Dibbo: but wait
[20:31, 12/6/2024] Dibbo: this song is amazing
[20:31, 12/6/2024] Dibbo: so I will stick to it
[20:31, 12/6/2024] Dibbo: send me some english song also
[20:31, 12/6/2024] Riyan: hold on
[20:31, 12/6/2024] Dibbo: I know what you are about to send
[20:32, 12/6/2024] Dibbo: 😂😂
[20:32, 12/6/2024] Riyan: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Dibbo: okok
[20:33, 12/6/2024] Riyan: Haan
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Dibbo who speaks Bengali as well as english. He is from Bangladesh and is a coder. You analyze chat history and respond like Dibbo"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)

