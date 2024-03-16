import streamlit as st
import time
from llm.textgenerator import generate_possible_text

def get_question():
    response = generate_possible_text()
    risk = response["risk"]
    generated_text = response["generated_text"]
    explanation = response["explanation"]
    return risk, generated_text, explanation

def initialize_session_state():
    session_state = st.session_state
    session_state.form_count = 0
    session_state.quiz_data = get_question()
    
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

        if 'form_count' not in st.session_state or 'quiz_data' not in st.session_state:
            initialize_session_state()
            
        if not st.session_state.quiz_data:
            st.seesion_state.quiz_data=get_question()

        quiz_data = st.session_state.quiz_data
        ans, qn, explanation = quiz_data

        st.markdown(f"Question:")
        lines = qn.split("\n")
        for line in lines:
            st.write(line)
        
        form = st.form(key=f"quiz_form_{st.session_state.form_count}")
        user_choice = form.radio("Choose an answer:", ("High", "Moderate", "Low"))
        submitted = form.form_submit_button("Submit your answer")
        
        if submitted:
            if is_correct_ans(user_choice, ans):
                st.success("Correct")
                st.balloons()
            else:
                st.error("Incorrect")
            st.markdown(f"Explanation: {explanation}")

            session_state = st.session_state
            session_state.quiz_data= get_question()

            another_question = st.button("Another question")
            
            if another_question:
                time.sleep(3)
                st.session_state.form_count += 1
            else:
                st.stop()