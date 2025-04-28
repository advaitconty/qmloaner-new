import google.generativeai as genai
<<<<<<< HEAD
import secret
=======

import secret as secrets

>>>>>>> 14a4fa61e99d0115735f85fea589154cce005f8c

def generate_gemini_response(prompt):
    try:
        genai.configure(api_key=secret.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Generated through a bit of testing with RP with Gemini
        default_prompt = (
            "You are an helpful assistant that will provide only storage instructions of guitars based on "
            "their models and cleaning instructions based on their models. The user input will be in the "
            "format of Guitar Model: {model name}, followed by weather the user wants cleaning instructions "
            "or storage instructions. also answer in plain text. Remember, this needs to be short and "
            "concise and within 70 words. If the user wants cleaning instructions, provide only the "
            "cleaning instructions. If the user wants storage instructions, provide only the storage "
            "instructions.")

        response = model.generate_content(f"{default_prompt} user input: {prompt}").text
    except Exception as e:
        response = "Handling directions not available. Please Google them yourselves."
        print("Error:\n{}".format(e))

    return response