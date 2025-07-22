import openai

openai.api_key = ""  # openai key

user_input = input("What is on your mind?: ")

# Call GPT-4 using the Chat Completions API
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": user_input}
    ]
)

# Print the AI's response
print("Tambarine AI says:\n")
print(response.choices[0].message.content.strip())
