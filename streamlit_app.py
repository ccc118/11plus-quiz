import streamlit as st
import pandas as pd
import random

# Sample DataFrame with words and synonyms
data = {
    'Word': ['happy', 'sad', 'fast', 'slow', 'big', 'small'],
    'Synonym1': ['joyful', 'unhappy', 'quick', 'lethargic', 'large', 'tiny'],
    'Synonym2': ['content', 'sorrowful', 'rapid', 'sluggish', 'huge', 'little'],
    'Synonym3': ['cheerful', 'mournful', 'speedy', 'unhurried', 'vast', 'miniature'],
    'Correct': ['joyful', 'unhappy', 'quick', 'lethargic', 'large', 'tiny']
}

df = pd.DataFrame(data)

# Function to generate a quiz question
def generate_question(df):
    row = df.sample().iloc[0]
    word = row['Word']
    correct_answer = row['Correct']
    options = [row['Synonym1'], row['Synonym2'], row['Synonym3']]
    random.shuffle(options)
    return word, correct_answer, options

st.title('Synonym Quiz for 11+ Exam Preparation')

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0

word, correct_answer, options = generate_question(df)

st.write(f"Select the synonym for the word: **{word}**")

user_answer = st.radio("Options:", options)

if st.button("Submit"):
    if user_answer == correct_answer:
        st.session_state.score += 1
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer is {correct_answer}.")
    
    st.session_state.question_count += 1

    st.write(f"Score: {st.session_state.score}/{st.session_state.question_count}")
    st.experimental_rerun()
