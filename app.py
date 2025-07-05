import streamlit as st
import random
import nltk
from nltk.corpus import words

# Function to generate a valid 4-letter English word
def generate_random_valid_word():
    nltk.download('words')
    word_list = words.words()
    four_letter_words = [word.lower() for word in word_list if len(word) == 4 and word.isalpha()]
    return random.choice(four_letter_words)

# Function to give hint (number of matching letters in correct position)
def get_hint(secret, guess):
    return sum([s == g for s, g in zip(secret, guess)])

# Page configuration
st.set_page_config(page_title="4-Letter Word Game", page_icon="🎯", layout="centered")

# Title and instructions
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🎯 4-Letter Word Guessing Game</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Guess a valid 4-letter English word</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Made by <b>Oshank Agrawal</b></p>", unsafe_allow_html=True)

with st.expander("🔍 Game Instructions"):
    st.write("""
    - A secret 4-letter word is selected.
    - You have 8 attempts to guess it.
    - After each guess, you'll see how many letters were in the correct position.
    - Past guesses and your score are tracked.
    """)

# --- Initialize session state ---
if "secret_word" not in st.session_state:
    st.session_state.secret_word = generate_random_valid_word()
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "past_guesses" not in st.session_state:
    st.session_state.past_guesses = []
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0

# Optional: Debug mode to see the word
st.write("Secret word:", st.session_state.secret_word)

# Input section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.session_state.attempts < 8 and not st.session_state.game_over:
        input_word = st.text_input("Your Guess", max_chars=4)

        if st.button("Submit"):
            if len(input_word) != 4 or not input_word.isalpha():
                st.warning("Please enter a valid 4-letter word.")
            else:
                guess = input_word.lower()
                st.session_state.attempts += 1
                hint = get_hint(st.session_state.secret_word, guess)
                st.session_state.past_guesses.append((guess, hint))

                if guess == st.session_state.secret_word:
                    st.success(f"🎉 Correct! The word was '{st.session_state.secret_word.upper()}'.")
                    st.balloons()
                    st.session_state.game_over = True
                    st.session_state.wins += 1
                else:
                    if st.session_state.attempts == 8:
                        st.session_state.game_over = True
                        st.session_state.losses += 1
                        st.error("💥 Game Over! You've used all 8 attempts.")
                        st.info(f"The correct word was: **{st.session_state.secret_word.upper()}**")
                    else:
                        st.warning(f"❌ Incorrect! Hint: {hint}/4 letters in correct position.")
    else:
        st.error("💥 Game Over! Click 'New Game' to play again.")
        st.info(f"The correct word was: **{st.session_state.secret_word.upper()}**")

# Show attempts
st.markdown(f"<p style='text-align:center;'>📝 Attempts: <b>{st.session_state.attempts}</b> / 8</p>", unsafe_allow_html=True)

# Show past guesses with hints
## --- Show Past Guesses in Real-time Matrix Grid ---
if st.session_state.past_guesses:
    st.markdown("### 🧩 Guess Grid:")

    for guess, _ in st.session_state.past_guesses:
        cols = st.columns(6)  # 4 letter cells + 2 hint cells

        secret_word = st.session_state.secret_word
        correct_pos = 0
        wrong_pos = 0
        used_indices = []

        # First pass: correct positions
        for i in range(4):
            if guess[i] == secret_word[i]:
                correct_pos += 1
                used_indices.append(i)

        # Second pass: correct letters but wrong positions
        for i in range(4):
            if guess[i] != secret_word[i] and guess[i] in secret_word:
                for j in range(4):
                    if (
                        guess[i] == secret_word[j]
                        and j not in used_indices
                        and guess[j] != secret_word[j]
                    ):
                        wrong_pos += 1
                        used_indices.append(j)
                        break

        # Render first 4 columns: letter boxes
        for i in range(4):
            cols[i].markdown(
                f"""
                <div style='
                    background-color:#f0f0f0;
                    text-align:center;
                    padding:12px;
                    border-radius:8px;
                    font-weight:bold;
                    font-size:22px;
                    border:1px solid #ccc'>
                    {guess[i].upper()}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Render 5th column: ✔ correct positions
        cols[4].markdown(
            f"""
            <div style='
                background-color:#d4edda;
                text-align:center;
                padding:12px;
                border-radius:8px;
                font-size:18px;
                font-weight:bold;
                border:1px solid #a3d8a3'>
                ✔ {correct_pos}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Render 6th column: 🕵 wrong position matches
        cols[5].markdown(
            f"""
            <div style='
                background-color:#fff3cd;
                text-align:center;
                padding:12px;
                border-radius:8px;
                font-size:18px;
                font-weight:bold;
                border:1px solid #ffeeba'>
                🕵 {wrong_pos}
            </div>
            """,
            unsafe_allow_html=True
        )

# Spacing after matrix
st.markdown("<br><br>", unsafe_allow_html=True)

# New Game Button (centered)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn3:
    if st.button("🔁 New Game"):
        st.session_state.secret_word = generate_random_valid_word()
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.past_guesses = []
        st.success("New game started!")


# Show score
st.markdown("---")
st.markdown("### 🏆 Scoreboard")
col_win, col_loss = st.columns(2)
with col_win:
    st.success(f"✅ Wins: {st.session_state.wins}")
with col_loss:
    st.error(f"❌ Losses: {st.session_state.losses}")
