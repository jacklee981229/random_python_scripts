import openai

openai.api_key = "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"

sentences = input("Enter text: ")
language = input("Enter language: ")

if language == "\n" or "" or " ":
    language = "mandarin"

prompt = f'Translate the sentence {sentences} in {language}'

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.1,
)

reply = response["choices"][0]["text"]
print(reply)

input()
