# 🎯 4-Letter Word Guessing Game

A fun, interactive word puzzle game built using [Streamlit](https://streamlit.io/), where you try to guess a valid 4-letter English word within 8 attempts. Inspired by Wordle, but with a custom hint system and clean grid layout!

---

## ✨ Features

- ✅ Random valid 4-letter word generated every game
- ⌛ Maximum of **8 attempts**
- 🔤 Real-time input with feedback
- 🧠 Smart hint system:
  - ✔ Count of letters in correct position
  - 🕵 Count of letters present but in wrong position
- 🧩 Visual matrix display of all past guesses
- 🏆 Score tracking (Wins & Losses across games)
- 🔁 “New Game” button to reset and play again

---

## 📸 Demo

![Game UI Screenshot](Guessing-Game/Screenshot.png) 

---

## 🚀 How to Run the App

### Prerequisites

- Python 3.7 or higher
- Streamlit
- nltk (Natural Language Toolkit)

### Installation

```bash
# Clone this repository
git clone https://github.com/OshankAgrawal/Guessing-Game.git
cd Guessing-Game

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate 

# Install dependencies
pip install -r requirements.txt


### Run the App

```bash
streamlit run app.py
```

---

## 🧠 How the Hint System Works

For every guess:

* `✔` tells how many letters are in the **correct position**.
* `🕵` tells how many letters are **correct but in the wrong position**.

> The actual correct letters are not revealed—only positional feedback is shown.

---

## 📁 Project Structure

```
.
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📚 Requirements

Here’s what the `requirements.txt` should contain:

```
streamlit
nltk
```

---

## 🛠️ To-Do / Possible Improvements

* [ ] Add difficulty levels (3-letter / 5-letter modes)
* [ ] Color-coded hint system (like Wordle)
* [ ] Leaderboard using database
* [ ] Mobile responsiveness
* [ ] Dark mode toggle

---

## 👨‍💻 Author

**Oshank Agrawal**
*Developer, Problem Solver, Tech Enthusiast*
🔗 [LinkedIn](https://www.linkedin.com/in/oshankagrawal/) • 📧 [oshankagrawal@example.com](mailto:oshankagrawal@example.com)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [NLTK Word Corpus](https://www.nltk.org/)
* All open-source developers and word game lovers ❤️
