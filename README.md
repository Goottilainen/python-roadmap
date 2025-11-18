# 🐍 Python Roadmap

A step-by-step learning journey through Python fundamentals, with practical mini-projects at each stage.

---

## 🧮 Mini Project 1: Calculator

My first interactive Python program.  
This calculator performs basic operations (`+`, `-`, `*`, `/`) and includes error handling for invalid inputs and division by zero.

### 📄 Files in this mini-project

| File | Description |
|------|--------------|
| `mini_project_calculator.py` | Performs addition, subtraction, multiplication, and division between two numbers entered by the user. Includes exception handling (`try` / `except`). |

---

### 💡 Example Output

*** My Mini Calculator Program ***

Type the first number: 8
Type the second number: 2
Select one of the following options: '+','-','*','/': *

The result of 8*2 is: 16


---

### ✅ Concepts Learned
- Input and output handling (`input()`, `print()`)
- Data type conversion (`int()`)
- Arithmetic operators (`+`, `-`, `*`, `/`)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling with `try` / `except`

---

## 🔁 Phase 2: Control Flow

This phase focuses on **decision making** and **loops** in Python.  
It includes conditional statements (`if`, `elif`, `else`), logical operators, and both `for` and `while` loops.  
The final mini-project combines everything into an interactive game.

---

### 📂 Files in this phase

| File | Description |
|------|--------------|
| `if_statements.py` | Classify a person's age as minor, adult, or senior. |
| `logical_operators.py` | Determine if someone can vote based on age and nationality. |
| `loops_for.py` | Use `for` loops to display and sum number sequences. |
| `loops_while.py` | Request numbers until the user types 0. |
| `mini_project_guess_game.py` | 🎮 **Guess The Number Game:** the user tries to guess a randomly generated number with hints and attempt count. |

---

### 🎮 Mini Project 2: Guess The Number Game

A small interactive Python game that challenges the player to guess a secret number between 1 and 10.

#### 🧠 Example Output

*** Guess The Number Game ***
I'm thinking of a number between 1 and 10...

Write your guess: 5
Too low! Try again.

Write your guess: 8
Too high! Try again.

Write your guess: 7
🎉 Correct! The number was 7.
You guessed it in 3 tries.


---

### ✅ Concepts Learned
- Conditional statements  
- Logical operators (`and`, `or`, `not`)  
- `for` and `while` loops  
- Counters and variables  
- Infinite loop control with `break`  
- Random number generation  

---

## 🧾 Phase 3: Lists, Tuples, and Dictionaries

This phase introduces **data structures** in Python to store and manipulate collections of information.  
The final mini-project implements a real-life example: a simple **To-Do List Manager**.

---

### 📂 Files in this phase

| File | Description |
|------|--------------|
| `lists_basics.py` | Add and remove fruits from a list. |
| `tuples_calendar.py` | Display days of the week using tuples. |
| `dictionaries_grades.py` | Calculate average, maximum, and minimum grades. |
| `sets_students.py` | Combine two sets of student names and find differences. |
| `mini_project_todo_list.py` | 🗒️ **Simple To-Do List:** manage your own list of tasks directly from the terminal. |

---

### 🗒️ Mini Project 3: Simple To-Do List

A beginner-friendly Python application to manage your daily tasks.  
You can view, add, or remove tasks, all through an interactive terminal menu.

#### 💡 Example Output

*** Simple To Do List ***

View tasks

Add task

Remove task

Exit

Type the number that you want to pick: 2
Write the task to add: Study Python
✅ 'Study Python' has been added successfully!

Type the number that you want to pick: 1

1. Study Python


---

### ✅ Concepts Learned
- Lists and indexing  
- Loops with `enumerate()`  
- Data validation and input handling  
- `append()` and `pop()` methods  
- Conditional flow inside loops  
- Simple user interface design (CLI)

---

📘 **End of Phase 3 – Next Step:** File handling (`open`, `read`, `write`) and basic data persistence.
