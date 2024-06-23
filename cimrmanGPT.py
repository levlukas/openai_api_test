from openai import OpenAI


def read_api_key():
    # Read the OpenAI API key from the .env file
    with open("API_KEY.env", "r") as file:
        key = file.read()
        print(f"fetching api key: {key}")
        return key


def read_cimrman_prompt():
    # Read the prompt from the .env file
    with open("CIMRMAN_PROMPT.env", "r", encoding='utf-8') as file:
        prompt = file.read()
        print(f"cimrman context loaded...")
        return prompt


def main():
    api_key = read_api_key()
    client = OpenAI(api_key=api_key)
    cimrman_context = read_cimrman_prompt()
    messages = [{'role': 'system', 'content': cimrman_context}]
    while True:
        message = input("User : ")
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

        reply = chat.choices[0].message.content
        print(f"CimrmanGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
