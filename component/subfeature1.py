import streamlit as st
import time
from llm.textgenerator import generate_possible_text

def get_question():
    scam_likelihood, generated_text = generate_possible_text()
    return scam_likelihood, generated_text

def initialize_session_state():
    session_state = st.session_state
    session_state.form_count = 0
    session_state.quiz_data = get_question()

# Define sub-feature component
# def sub_feature():
#     st.subheader('Test your scam detecting skills', divider='rainbow')
#     caption = (
#         "Ready to Put Your Phishing Scam Radar to the Test? Dive into Our Interactive Educational Quiz Section! "
#         "Here, you'll embark on a journey of discovery, where real-world scenarios challenge your ability to spot phishing attempts. "
#         "Learn to distinguish between genuine communications and deceptive tactics, empowering yourself to safeguard your online presence."
#     )
#     st.caption(caption)
    
#     if "quiz_started" not in st.session_state:
#         st.session_state.quiz_started = False
    
#     if st.button("Generate Question", type="primary"):
#         # Display quiz
#         st.session_state.quiz_started = True

#     if st.session_state.quiz_started:
#         display_quiz()

# def display_quiz():
#     global user_choice
    
#     # Generate possible scam text
#     # show loading
#     progress_bar = st.progress(0)
#     progress_text = "Generating quiz... Please wait..."

#     for i in range(39):
#         time.sleep(0.07)
#         progress_bar.progress(i + 1, progress_text)

#     scam_likelihood, generated_text = generate_possible_text()

#     for i in range(30):
#         time.sleep(0.07)
#         progress_bar.progress(i + 71, progress_text)
    
#     progress_bar.empty()
#     st.write("Refer to the generated text below:")
#     st.write(generated_text)
    
#     # Add radio buttons for user to select their choice
#     user_choice = st.radio("What is the likelihood that this is a scam?", ("High", "Moderate", "Low"))
#     pressed = st.button("Submit Answer")
#     while not pressed:
#         continue
#     if pressed:
#         # Provide feedback based on user's choice
#         quiz_feedback = provide_feedback(user_choice, scam_likelihood)
#         st.write("Feedback:")
#         st.write(quiz_feedback)
    

# Function to provide feedback for sub-feature
# TODO: Add more feedback options for better user experience / make it more educational
# def provide_feedback(user_choice, scam_likelihood):
#     if user_choice.lower() in scam_likelihood.lower():
#         return "Correct! You have a keen eye for scams."
#     else:
#         return "Incorrect. Keep practicing to improve your scam detection skills."
    
def is_correct_ans(user_choice, correct_answer):
    if user_choice.lower() in correct_answer.lower():
        return True
    else:
        return False

def sub_feature():
    st.subheader('Test your scam detecting skills', divider='rainbow')
    caption = (
        "Ready to Put Your Phishing Scam Radar to the Test? Dive into Our Interactive Educational Quiz Section! "
        "Here, you'll embark on a journey of discovery, where real-world scenarios challenge your ability to spot phishing attempts. "
        "Learn to distinguish between genuine communications and deceptive tactics, empowering yourself to safeguard your online presence."
    )
    st.caption(caption)    

    if st.button("Generate Question", type="primary") or 'form_count' in st.session_state:
        if 'form_count' not in st.session_state:
            initialize_session_state()
            
        if not st.session_state.quiz_data:
            st.seesion_state.quiz_data=get_question()

        quiz_data = st.session_state.quiz_data
        ans, qn = quiz_data

        st.markdown(f"Question: {qn}")
        
        form = st.form(key=f"quiz_form_{st.session_state.form_count}")
        user_choice = form.radio("Choose an answer:", ("High", "Moderate", "Low"))
        submitted = form.form_submit_button("Submit your answer")
        
        if submitted:
            if is_correct_ans(user_choice, ans):
                st.success("Correct")
            else:
                st.error("Incorrect")
            st.markdown(f"Explanation: The likelihood of scam is {ans}")
            
            another_question = st.button("Another question")
            
            session_state = st.session_state
            session_state.quiz_data= get_question()

            if another_question:
                st.session_state.form_count += 1
            else:
                st.stop()