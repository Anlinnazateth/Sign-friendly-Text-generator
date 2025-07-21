"""Sign-Friendly Text Generator — Streamlit application.

Converts English sentences into sign-language-friendly text by removing
stopwords and simplifying grammar.
"""

import streamlit as st
from utils import sign_friendly_convert

st.set_page_config(
    page_title="Sign-Friendly Text Generator",
    page_icon="🤟",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("🤟 About")
st.sidebar.markdown(
    """
    This tool converts English text into **sign-language-friendly** output
    by removing common words (stopwords) like *is*, *the*, *and*, etc.

    Sign languages use simplified grammar structures that focus on
    content words — nouns, verbs, adjectives — rather than function words.

    **How it works:**
    1. Tokenize the input using NLTK
    2. Remove punctuation and non-alphabetic tokens
    3. Filter out English stopwords
    4. Return the simplified text
    """
)

st.sidebar.markdown("### Options")
show_removed = st.sidebar.checkbox("Show removed words", value=False)
show_stats = st.sidebar.checkbox("Show statistics", value=True)

EXAMPLES = [
    "I will be going to the market tomorrow.",
    "The quick brown fox jumps over the lazy dog.",
    "She is reading a very interesting book about science.",
    "We are not going to the park because it is raining.",
    "Can you please tell me where the nearest hospital is?",
]

st.sidebar.markdown("### Examples")
example = st.sidebar.selectbox("Try an example:", [""] + EXAMPLES)

# ---------------------------------------------------------------------------
# Main UI
# ---------------------------------------------------------------------------
st.title("🤟 Sign-Friendly Text Generator")
st.markdown("Convert English sentences into sign-language-friendly text.")

# Single sentence input
sentence = st.text_input("Enter an English sentence:", value=example)

if sentence:
    result = sign_friendly_convert(sentence)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Original:**")
        st.info(result["original"])
    with col2:
        st.markdown("**Sign-Friendly:**")
        st.success(result["simplified"] if result["simplified"] else "*(empty — all words removed)*")

    if show_stats:
        c1, c2, c3 = st.columns(3)
        c1.metric("Original Words", result["word_count_original"])
        c2.metric("Simplified Words", result["word_count_simplified"])
        c3.metric("Reduction", f"{result['reduction_percentage']}%")

    if show_removed and result["removed_words"]:
        st.markdown(f"**Removed words:** {', '.join(result['removed_words'])}")

# ---------------------------------------------------------------------------
# Multi-sentence input
# ---------------------------------------------------------------------------
st.markdown("---")
st.subheader("Batch Conversion")
multi_text = st.text_area(
    "Enter multiple sentences (one per line):",
    height=150,
    placeholder="I am going to the store.\nShe was reading a book.\nThey will not come today.",
)

if multi_text.strip():
    lines = [line.strip() for line in multi_text.strip().split("\n") if line.strip()]
    rows = []
    for line in lines:
        r = sign_friendly_convert(line)
        rows.append({
            "Original": r["original"],
            "Simplified": r["simplified"],
            "Reduction": f"{r['reduction_percentage']}%",
        })
    st.dataframe(rows, use_container_width=True)
