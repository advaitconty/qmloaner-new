import anthropic

def generate_gemini_response(prompt):
    # try:
    client = anthropic.Anthropic(api_key="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")

    # Generated through a bit of testing with RP with Gemini
    default_prompt = (
        "You are an helpful assistant that will provide only storage instructions of guitars based on "
        "their brand and cleaning instructions based on their brand. The user input will be in the "
        "format of Guitar Model: {model name}, followed by weather the user wants cleaning instructions "
        "or storage instructions. also answer in plain text. Remember, this needs to be short and "
        "concise and within 70 words. If the user wants cleaning instructions, provide only the "
        "cleaning instructions. If the user wants storage instructions, provide only the storage "
        "instructions, not in point form")

    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        temperature=1,
        system=default_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    ).content[0].text
    # except Exception as e:
    #     # response = "Handing directions not available at time of generation. Sorry for the inconvinence caused!"
    #     response = str(Exception)
 
    return response

if __name__ == "__main__":
    print(generate_gemini_response("Alhambra 4P, Cleaning Instructions"))