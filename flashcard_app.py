import streamlit as st
import pandas as pd
import tempfile
import os
from parser import load_resume as load_text
from generator import generate_flashcards

st.set_page_config(page_title="AI Flashcard Generator", layout="centered")
st.title("AI Flashcard Generator")
st.caption("Upload a PDF or TXT file and generate flashcards instantly.")

with st.sidebar:
    st.header("Settings")
    num_cards = st.slider("Number of flashcards", 5, 20, 10)

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    text = load_text(tmp_path)
    os.unlink(tmp_path)

    st.success(f"Extracted {len(text)} characters from {uploaded_file.name}")

    if st.button("Generate Flashcards", type="primary"):
        with st.spinner("Generating flashcards..."):
            cards = generate_flashcards(text, num_cards)

        if not cards:
            st.error("Failed to generate flashcards. Try a different document.")
            st.stop()

        st.session_state["cards"] = cards
        st.session_state["index"] = 0
        st.session_state["flipped"] = False

if "cards" in st.session_state:
    cards = st.session_state["cards"]
    index = st.session_state["index"]
    flipped = st.session_state["flipped"]
    current = cards[index]

    st.divider()
    st.markdown(f"**Card {index + 1} of {len(cards)}**")

    with st.container(border=True):
        if flipped:
            st.markdown(f"**A:** {current['answer']}")
        else:
            st.markdown(f"**Q:** {current['question']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("← Prev") and index > 0:
            st.session_state["index"] -= 1
            st.session_state["flipped"] = False
            st.rerun()

    with col2:
        if st.button("Flip"):
            st.session_state["flipped"] = not flipped
            st.rerun()

    with col3:
        if st.button("Next →") and index < len(cards) - 1:
            st.session_state["index"] += 1
            st.session_state["flipped"] = False
            st.rerun()

    st.divider()
    df = pd.DataFrame(cards)
    csv = df.to_csv(index=False)
    st.download_button("Download Cards CSV", csv, "flashcards.csv", "text/csv")