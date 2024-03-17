import streamlit as st
import pandas as pd
import altair as alt

def home_component():

    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("logo_1.png", output_format='PNG')

    st.subheader("Welcome to Bandicota.ai - Your Ultimate Defense Against Phishing Scams")

    st.write("Did you know that phishing attacks are the most common form of cybercrime globally, with millions of attempts occurring every day? At Bandicota.ai, we're committed to keeping you safe from these threats.")

    st.subheader("**Stay Informed:**")

    # Define the phishing statistics data
    data = pd.DataFrame({
        'Scam Fields': ['Online Shopping', 'Tech Support', 'Email Compromise', 'Investment Scams', 'Romance Scams'],
        'Financial Losses (USD millions)': [100, 300, 500, 200, 400]
    })

    # Create a bar chart
    chart = alt.Chart(data).mark_bar().encode(
        x= alt.X('Scam Fields', axis=alt.Axis(labelAngle=0)),
        y='Financial Losses (USD millions)'
    ).properties(
        width=600,
        height=400,
    )

    # Display the bar chart
    st.altair_chart(chart, use_container_width=True)