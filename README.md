# Expense Tracker (Console-Based Python Application)

## Overview

Expense Tracker is a console-based Python application that helps users manage their daily expenses efficiently. The application allows users to add, view, update, and delete expenses while also setting category-wise budgets and monitoring spending habits.

The project uses SQLite as the database to store expense and budget information permanently, making it a lightweight and practical personal finance management tool.

---

## Features

### Expense Management

* Add new expenses
* View all expenses
* Update existing expenses
* Delete expenses

### Budget Management

* Set category-wise budgets
* View all budgets
* Track spending against budgets
* Automatic budget warnings

### Smart Budget Alerts

* Warning when spending reaches 80% of the allocated budget
* Alert when budget is exceeded

### Data Persistence

* Stores all data in SQLite database
* No data loss after program termination

---

## Technologies Used

* Python 3
* SQLite3
* Datetime Module

---

## Project Structure

```text
Expense_Tracker/
│
├── main.py
├── database.py
├── expenses.db
└── README.md
```

---

## Database Schema

### Expenses Table

| Column      | Type                  |
| ----------- | --------------------- |
| id          | INTEGER (Primary Key) |
| date        | TEXT                  |
| category    | TEXT                  |
| amount      | REAL                  |
| description | TEXT                  |

### Budgets Table

| Column   | Type               |
| -------- | ------------------ |
| category | TEXT (Primary Key) |
| budget   | REAL               |

---

## Menu Options

```text
1. Add Expense
2. View Expenses
3. Delete Expense
4. Update Expense
5. Set Budget
6. View Budgets
7. Check Budget
8. Exit
```

---

## Sample Usage

### Add Expense

```text
Enter Category: Food
Enter Amount: 250
Enter Description: Burger

Expense Added Successfully!
```

### Set Budget

```text
Enter Category: Food
Enter Budget Amount: 3000

Budget Set Successfully!
```

### Budget Warning

```text
Warning: Food Budget is 85.0% Used
```

### Budget Exceeded

```text
Budget Exceeded for Food
```

---

## How to Run

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to Project Directory

```bash
cd Expense_Tracker
```

### Run the Application

```bash
python main.py
```

---

## Learning Outcomes

This project demonstrates:

* CRUD Operations
* SQLite Database Integration
* Modular Programming
* Python Functions
* Database Design
* Budget Tracking Logic
* Data Validation
* Console-Based User Interfaces

---

## Future Enhancements

* Dashboard with spending analytics
* Monthly reports
* CSV export functionality
* Search expenses by category
* Search expenses by date
* Expense statistics and visualizations
* AI-based spending suggestions
* User authentication system

---

## Author

Aryan Pandey

Built as a practical Python and SQLite project to learn database-driven application development and personal finance management.
