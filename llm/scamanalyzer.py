import time  # for measuring time duration of API calls
from openai import OpenAI
from llm.client import client


# Function to analyze text for scam likelihood and provide next steps
def analyze_text_for_scam(text):

    # Define the prompt structure
    prompt = (
        f"Input text: {text}\n"
        "You must reply in the following structure\n"
        "Likelihood of being a scam:\n"
        "Analysis Report:\n\n"
        "Next Steps:\n1.\n2.\n"
    )


    system_prompt = (
        "I need assistance in analyzing text for scam detection, specifically phishing scams. "
        "The response should include a structured analysis report indicating the likelihood of a scam and providing next steps. "
        "Please ensure that the response follows the specified structure for ease of parsing and integration with the application."
    )

    start_time = time.time()
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
    # calculate the time it took to receive the response
    response_time = time.time() - start_time

    # Extract the generated response from the API
    generated_text = response.choices[0].message.content
    print("\n\ngenerated_text: ", generated_text)

    # Extract the likelihood of being a scam and the analysis report
    split_text = generated_text.split("Analysis Report:")
    scam_likelihood = split_text[0].split("Likelihood of being a scam:")[1].strip()
    generated_text = split_text[1]
    print("\n\nscam_likelihood: ", scam_likelihood)

    return scam_likelihood, generated_text, response_time