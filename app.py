import streamlit as st
from component.mainfeature import main_feature
from component.subfeature1 import sub_feature

def header():
    st.title("Bandicota.ai")
    # Add a description
    caption = (
        "Powered by LLM (Large Language Model), our app serves as your vigilant guardian, analyzing text for potential scam indicators. "
        "Beyond detection, we are committed to educating and empowering users to recognize and combat scams effectively. "
        "Join us in the fight against fraudulent schemes and stay one step ahead in safeguarding your online presence."
    )

    st.caption(caption)


# Main app layout
def main():
    # Render header component
    header()

    # Render main feature component
    main_feature()

    # add some space maybe
    
    # Render sub-feature component
    sub_feature()

if __name__ == "__main__":
    main()
