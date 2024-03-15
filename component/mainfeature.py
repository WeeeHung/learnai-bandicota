import streamlit as st
import time
from llm.scamanalyzer import analyze_text_for_scam

def likelihood_to_color(likelihood):
    message = f"Risk: {likelihood}"
    if "high" in likelihood.lower():
        st.error(message)
    elif "moderate" in likelihood.lower():
        st.warning(message)
    elif "low" in likelihood.lower():
        st.success(message)
    else:
        st.info(message)



def analyze_and_display(user_input):
    progress_bar = st.progress(0)
    progress_text = "Analyzing... Please wait..."

    for i in range(69):
        time.sleep(0.07)
        progress_bar.progress(i + 1)
    
    progress_bar.progress(70, progress_text)
    scam_likelihood, scam_report, response_time = analyze_text_for_scam(user_input)

    for i in range(30):
        time.sleep(0.07)
        progress_bar.progress(i + 71, progress_text)
    
    progress_bar.empty()

    # TODO: Some Error Handling (?)

    st.success(f"Scam analysis completed in {response_time:.2f} seconds")
    
    with st.expander("Analysis Report"):
        likelihood_to_color(scam_likelihood)
        st.write(scam_report)
    
   

# Define main feature component
def main_feature():
    st.subheader('Scam Detector', divider='rainbow')
    # Input for checking if scam
    user_input = st.text_area("Enter text to check if it's a scam")

    if st.button("Check for Scam", use_container_width=True):
        # Perform analysis and provide report
        analyze_and_display(user_input)