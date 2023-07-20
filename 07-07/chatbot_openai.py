import openai
import json

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define a function to interact with the ChatGPT model
def chat_with_gpt(prompt):
  response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=50,
    temperature=0.7,
    n=1,
    stop=None,
    timeout=10
    )
  reply = response.choices[0].text.strip()
  return reply

# Main loop for chatting with the bot
print("ChatGPT: Hello! How can I assist you today?")
while True:
  user_input = input("User: ")

    # Stop the loop if the user says 'bye'
  if user_input.lower() == 'bye':
    print("ChatGPT: Goodbye!")
    break

    # Generate a response from ChatGPT
  prompt = "User: " + user_input + "\nChatGPT:"
  reply = chat_with_gpt(prompt)

    # Display the response
  print(reply)