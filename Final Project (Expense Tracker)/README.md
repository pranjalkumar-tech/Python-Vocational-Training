# Expense Tracker

A simple **Expense Tracker desktop application** built using Python, Tkinter, and SQLite3.

The project was developed as the **Final Project** for Python Vocational Training and has also been packaged as a **Windows `.exe` application**, so it can be opened directly without running the Python source code.

## Features

- Add new expenses
- Update existing expenses
- Delete expenses
- Select expense records from the table
- View all saved expenses
- Calculate and display total spending
- Expense categories:
  - Food
  - Transport
  - Bills
  - Shopping
  - Other
- Store expense data using SQLite3
- Simple dark-themed graphical interface
- Available as a Windows `.exe` application

## Technologies Used

- **Python**
- **Tkinter** - For the graphical user interface
- **SQLite3** - For storing expense records
- **PyInstaller** - Used to create the Windows `.exe` application

## Project Files

```text
Final Project/
│
├── Expense_Tracker_Final_Project.py
├── Expense_Tracker_Final_Project.exe
└── README.md
```

### File Description

- `Expense_Tracker_Final_Project.py` - Main Python source code
- `Expense_Tracker_Final_Project.exe` - Windows application that can be opened directly
- `README.md` - Project documentation

## How to Run the Project

### Option 1 - Run the Windows Application

Open:

```text
Expense_Tracker_Final_Project.exe
```

The application will start directly.

### Option 2 - Run the Python Code

If Python is installed, open the Python file:

```text
Expense_Tracker_Final_Project.py
```

Or run it from the terminal:

```bash
python Expense_Tracker_Final_Project.py
```

## Database

The project uses **SQLite3** to store expense records.

When the application is run, an `expenses.db` database file is created automatically if it does not already exist.

The database stores:

- Expense ID
- Amount
- Category
- Date
- Note

The database file is created automatically by the application and does not need to be included in the project repository.

## How the Project Works

1. The user enters the expense amount.
2. The user selects a category.
3. The user enters the date and an optional note.
4. The expense is saved in the SQLite database.
5. Saved expenses are displayed in the table.
6. The user can select a record to update or delete it.
7. The total spending is calculated and displayed.

## Concepts Used

This project demonstrates the following Python concepts:

- Variables
- Input and output
- Conditional statements
- Functions
- Exception handling
- File/database handling
- SQLite3
- Tkinter GUI
- Events and buttons
- Treeview
- Basic CRUD operations
- Python application packaging

## Final Project Statement

**Expense Tracker** is a simple desktop application that helps users record, view, update, and delete their daily expenses.

The project combines **Python, Tkinter, and SQLite3** into a practical application and is packaged as a **Windows `.exe` application** for easy use.
