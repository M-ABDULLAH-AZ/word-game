import streamlit as st
import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

words = ['streamlit', 'python', 'data', 'science', 'machine', 'learning', 'artificial', 'intelligence','pakistan','lahore',"islamabad",'antartica','combination','atmosphere','circumference','karachi','free fire','minecraft']

if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.scrambled_word = scramble_word(st.session_state.word)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'correct' not in st.session_state:
    st.session_state.correct = False

st.title('Word Scramble Game')

st.write(f'Scrambled word: {st.session_state.scrambled_word}')

user_guess = st.text_input('Your guess:')

if st.button('Submit'):
    st.session_state.attempts += 1
    if user_guess.lower() == st.session_state.word:
        st.session_state.correct = True

if st.session_state.correct:
    st.write(f'Congratulations! You guessed the word "{st.session_state.word}" correctly in {st.session_state.attempts} attempts.')
    if st.button('Play Again'):
        st.session_state.word = random.choice(words)
        st.session_state.scrambled_word = scramble_word(st.session_state.word)
        st.session_state.attempts = 0
        st.session_state.correct = False
else:
    st.write(f'Attempts: {st.session_state.attempts}')

