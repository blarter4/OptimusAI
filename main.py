from openai import OpenAI
Usr_input = ""
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "You do not repeat anything back except for the code that you are given optimized. When you receive the code, you optimize it written in the target language for that system. You are to say nothing until you receive the code. You return the code and that is it, make sure everything functions exactly as before."
      }
      {
        "role": "user", 
        "content": Usr_input + " " + 
      }
    ]
)
optcode = completion.choices[0].message.content 
#Here is where I left off, I need to make it so that the Usr_input is constant, and the code from the file is read, parsed as a string and sent to chatgpt, its file location needs to be stored so it can save it as the original name in a copied file system of the game. ChatGPT needs to receive the user prompt every time, and each time it needs to be added to the source code of the next file in the recursion loop. 