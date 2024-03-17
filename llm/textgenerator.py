from openai import OpenAI
import random
import re
from llm.client import client

def generate_possible_text():

    # TODO: Include explanation or smth (make it educational), teach like they are 5
    # Define the prompt structure
    risk_levels = ["low", "moderate", "high"]
    topics = ["school", "work", "family", "friends", "shopping", "banking", "social media", "government", 
              "health", "insurance", "travel", "entertainment", "dating", "housing", "charity"]
    format = [

        {"type": "email",
        "format": ("Generated Text: \\n Sender email: [x] \\n title: [x] \\n body: [x] \\n"
        "Explanation: xxx")},

        {"type": "text message",
         "format": ("Generated Text: xxx"
        "Explanation: xxx")}

    ]
    rand_chosen_risk_level = random.choice(risk_levels)
    rand_chosen_format = random.choice(format)
    chosen_type = rand_chosen_format["type"]
    chosen_format = rand_chosen_format["format"]
    chosen_topic = random.choice(topics)
    
    prompt = (
        f"Generate a new {chosen_type} regarding {chosen_topic} in no longer than 150 words."
        f"It's likelihood of being a scam is {rand_chosen_risk_level}\n"
        "Your generated text must fit the given risk level and type.\n"
        "Respond in the following structure\n"
        f"{chosen_format}\n"
        "Your explanation should be educational and easy to understand."
    )

    system_prompt = (
        "I need assistance for generating a scam detection quiz, so you will generate emails and text messages that are of various risk levels: low, moderate, high, you must also strictly follow the structure. "
        "In order to not hint the user, the message should not include give-away words like 'scam', 'phishing', 'fraud', etc."
        "For text messages: \\n"
        "Generated Text: xxx \\n"
        "Explanation: xxx \\n"
        "For emails: \\n"
        "Generated text: \\n Sender email: x \\n title: x \\n body: x \\n "
        "Explanation: xxx \\n"
        "You can use example.com if you want to include links."
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

    scam_likelihood = rand_chosen_risk_level
    explanation = f"The risk level is {rand_chosen_risk_level}" # default explanation

    # parse generated text
    split_text = generated_text.split("Explanation:")
    generated_text = split_text[0].replace("Generated Text:", "").strip()
    explanation = split_text[1]

    

    return {"risk": scam_likelihood, "generated_text": generated_text, "explanation": explanation}