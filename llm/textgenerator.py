from openai import OpenAI
from llm.client import client

def generate_possible_text():

    # TODO: Include explanation or smth (make it educational), teach like they are 5
    # Define the prompt structure
    prompt = (
        "Generate an email or text message no longer than 150 words."
        "It can have a likely scam content, such as a phishing scam, with a likelihood of high, moderate or low\n"
        "If it is email, include the sender's email, subject line and the body of the email, each with new line\n"
        "If it is a text message, include the sender's phone number and the body of the text message with new line\n"
        "Respond in the following structure\n"
        "Likelihood of scam:\n"
        "Generated Text:\n\n"
    )


    system_prompt = (
        "I need assistance in generating text for scam detection quiz, specifically phishing scams. "
        "The response should include a structured analysis report indicating the likelihood of a scam and the generated email or letter. "
        "Do not include words such as scam, phishing, fraud, etc. in the generated text."
        "Do not give advice on how to avoid scams as it will hint the user for the correct answer."
        "use example.com if you need to include a website in the generated text."
        "Add \\n where you want to start a new line."
        "Please ensure that the response follows the specified structure for ease of parsing and integration with the application."
    )

    # Call the OpenAI API with the GPT-3.5-turbo-0125 model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        # max_tokens=150
    )

    # Extract the generated response from the API
    generated_text = response.choices[0].message.content
    print("\n\ngenerated_text: ", generated_text)

    # Extract the likelihood of being a scam and the analysis report
    split_text = generated_text.split("Generated Text:")
    scam_likelihood = split_text[0].split("Likelihood of scam:")[1].strip()
    # remove the words "Generated Text:" from the generated text
    generated_text = split_text[1].replace("Generated Text:", "").strip()
    print("\n\nscam_likelihood: ", scam_likelihood)

    return scam_likelihood, generated_text