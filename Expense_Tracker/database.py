import sqlite3
from datetime import datetime


def connect_db():
    conn = sqlite3.connect("expenses.db")
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Expenses Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)

    # Budgets Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT PRIMARY KEY,
            budget REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# =========================
# Expense Functions
# =========================

def add_expense(category, amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO expenses(date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))

    conn.commit()
    conn.close()


def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    conn.close()

    return expenses


def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()


def update_expense(expense_id, category, amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET category = ?,
            amount = ?,
            description = ?
        WHERE id = ?
    """, (category, amount, description, expense_id))

    conn.commit()
    conn.close()


# =========================
# Budget Functions
# =========================

def set_budget(category, budget):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO budgets(category, budget)
        VALUES (?, ?)
        ON CONFLICT(category)
        DO UPDATE SET budget = excluded.budget
    """, (category, budget))

    conn.commit()
    conn.close()


def view_budgets():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM budgets")

    budgets = cursor.fetchall()

    conn.close()

    return budgets


def get_category_spending(category):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE category = ?
    """, (category,))

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0


def check_budget(category):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT budget
        FROM budgets
        WHERE category = ?
    """, (category,))

    result = cursor.fetchone()

    conn.close()

    if not result:
        return

    budget = result[0]
    spent = get_category_spending(category)

    percentage = (spent / budget) * 100

    if percentage >= 100:
        print(f"\n❌ Budget Exceeded for {category}")

    elif percentage >= 80:
        print(f"\n⚠ Warning: {category} Budget is {percentage:.1f}% Used")


def get_total_spending():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0

def get_total_budget():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(budget)
        FROM budgets
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0

def get_top_category():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category,
               SUM(amount) as total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    conn.close()

    return result

def show_dashboard():
    total_budget = get_total_budget()
    total_spent = get_total_spending()

    remaining = total_budget - total_spent

    percentage = 0

    if total_budget > 0:
        percentage = (total_spent / total_budget) * 100

    bars = int(percentage // 5)

    print("\n" + "=" * 40)
    print("         EXPENSE DASHBOARD")
    print("=" * 40)

    print(f"Total Budget     : ₹{total_budget:.2f}")
    print(f"Total Spent      : ₹{total_spent:.2f}")
    print(f"Remaining Budget : ₹{remaining:.2f}")
    print(f"Usage            : {percentage:.1f}%")

    print("\nProgress:")

    print(
        "[" +
        "#" * bars +
        "-" * (20 - bars) +
        "]"
    )

    top = get_top_category()

    if top:
        print(
            f"\nTop Category : {top[0]} (₹{top[1]:.2f})"
        )

    print("=" * 40)



def search_by_category(category):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE category = ?
    """, (category,))

    result = cursor.fetchall()

    conn.close()

    return result

def search_by_date(date):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE date = ?
    """, (date,))

    result = cursor.fetchall()

    conn.close()

    return result

