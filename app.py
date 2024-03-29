import streamlit as st
from component.mainfeature import main_feature
from component.subfeature1 import sub_feature
from component.homefeature import home_component

def header():
    st.title("Bandicota.ai")
    # Add a description
    caption = (
        "Powered by LLM (Large Language Model), our app serves as your vigilant guardian, analyzing text for potential scam indicators. "
        "Beyond detection, we are committed to educating and empowering users to recognize and combat scams effectively. "
        "Join us in the fight against fraudulent schemes and stay one step ahead in safeguarding your online presence."
    )
    st.caption("Better Safe than Sorry.")
    st.caption(caption)

def config():
    st.set_page_config(
        page_title="Bandicota.ai - Scam Analyzer",
        page_icon=":rat:",
    )

# Main app layout
def main():
    
    config()
    # Render header component
    header()

    home, detection, education = st.tabs(["Home", "Detection", "Education"])

    # Render home component
    with home:
        home_component()

    # Render main feature component
    with detection:
        main_feature()
    
    # Render sub-feature component
    with education:
        sub_feature()

if __name__ == "__main__":
    main()
