# 🐍 Snake–Water–Gun Game (Python)

A beginner-friendly **Snake–Water–Gun** game developed in **Python**, where a user plays against the computer.  
The game includes realistic delays, clear result logic, and a feedback system that saves user responses to a file.

---

## 🎯 Game Objective

Choose between **Snake**, **Water**, or **Gun** and try to defeat the computer’s randomly generated choice based on predefined rules.

---

## 📜 Game Rules

| Player Choice | Computer Choice | Result |
|--------------|----------------|--------|
| Snake        | Water          | Win    |
| Water        | Gun            | Win    |
| Gun          | Snake          | Win    |
| Same choice  | Same choice    | Draw   |

---

## ⚙️ How the Game Works

1. The computer randomly selects one option:
   - Snake
   - Water
   - Gun

2. The user enters their choice using text input:
   - `snake`
   - `water`
   - `gun`

3. The program:
   - Converts choices into numeric values for easy comparison
   - Displays both choices
   - Uses time delays for better user experience
   - Determines and displays the result (Win / Lose / Draw)

4. After the game ends:
   - The user provides their name and feedback
   - Feedback is saved in a text file automatically

---

## 🛠️ Technologies & Concepts Used

- **Python 3**
- `random` module → computer choice
- `time` module → delay effects
- Dictionaries → game logic mapping
- Conditional statements → result calculation
- File handling → feedback storage

---

## 💾 Feedback System

After gameplay, the user is asked to submit feedback.  
The feedback is stored in a file named:

