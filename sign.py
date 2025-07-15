import streamlit as st
import nltk
from nltk.corpus import stopwords

def simple_sign_friendly(text):
    # Use a simple split method to tokenize the text
    tokens = text.split()  # Tokenizes based on spaces (simpler approach)
    stop_words = set(stopwords.words("english"))
    filtered = [w for w in tokens if w.lower() not in stop_words and w.isalpha()]
    return " ".join(filtered)

# Streamlit UI
st.set_page_config(page_title="Sign-Friendly Sentence Converter", layout="centered")
st.title("🧏‍♀️ Sign-Friendly Sentence Converter")

sentence = st.text_input("Enter an English sentence:")

if sentence:
    output = simple_sign_friendly(sentence)
    st.markdown("### Sign Language Friendly Output:")
    st.success(output)