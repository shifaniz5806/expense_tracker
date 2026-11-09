# Expense Tracker 💰

A simple, menu-driven Expense Tracker built using Python. This project allows users to record and manage their daily expenses, calculate total spending, search expenses by category, and view spending summaries.

## 📌 Features

The Expense Tracker provides the following features:

1. **Add an Expense:** Record an expense by entering its name, amount, category, and date.
2. **View All Expenses:** Display all the expenses recorded.
3. **Calculate Total Expenses:** Calculate the total amount spent using recursion.
4. **Search by Category:** Find expenses belonging to a specific category.
5. **Find Highest Expense:** Identify the expense with the highest amount.
6. **View Expense Summary:** Calculate and display the total spending for each category.
7. **Exit:** Safely exit the program.

## 🛠️ Technologies Used

- Python 3
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Recursion

## ⚙️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/expense_tracker.git
   ```

2. Navigate to the project folder:

   ```bash
   cd expense_tracker
   ```

3. Run the Python file:

   ```bash
   python main.py
   ```

## 📖 How It Works

When the program runs, users are presented with a menu containing seven options. They can select an option by entering its corresponding number.

Each expense is stored as a dictionary containing:
- Name
- Amount
- Category
- Date

These dictionaries are stored in a list, allowing the program to manage multiple expenses.

The project also uses recursion to calculate the total expenses and loops to search, compare, and summarize expense records.

## 💡 Concepts Practiced

This project was developed to practise fundamental Python programming concepts, including:

- Creating and calling functions
- Working with lists and dictionaries
- Iterating through data using loops
- Using conditional statements
- Implementing recursion
- Searching and comparing values
- Basic data management

## 🚀 Future Improvements

Possible improvements for future versions include:

- Save expenses permanently using file handling.
- Add options to edit and delete expenses.
- Generate monthly and weekly expense reports.
- Display spending statistics using charts.
- Add a graphical user interface (GUI).

## 👩‍💻 Author

Created as a beginner Python mini-project to strengthen programming fundamentals and practical problem-solving skills.

---

**Note:** Currently, expenses are stored in memory using Python lists and dictionaries. All recorded data is lost when the program exits.
