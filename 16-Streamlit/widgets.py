import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')
name = st.text_input('Enter Your Name')
age = st.slider('Select Your Age',0,100,25)
if name:
    st.write(f"Hello, {name}")
st.write (f"Your age is {age}")
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your for language", options)
st.write(f"You selected {choice}")

data = {
    "Name" : ["Shruti", "Anuj", "Shravani"],
    "Age" : [21, 16, 16],
    "City" : ["Thane", "Thane", "Thane"]
}
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)