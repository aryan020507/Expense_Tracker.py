from database import (
    create_table,
    add_expense,
    view_expenses,
    delete_expense,
    update_expense,
    set_budget,
    view_budgets,
    check_budget
)

create_table()

while True:

    print("\n" + "=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Set Budget")
    print("6. View Budgets")
    print("7. Check Budget")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # ====================
    # Add Expense
    # ====================

    if choice == '1':

        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        description = input("Enter Description: ")

        add_expense(
            category,
            amount,
            description
        )

        check_budget(category)

        print("\n✅ Expense Added Successfully!")

    # ====================
    # View Expenses
    # ====================

    elif choice == '2':

        expenses = view_expenses()

        if not expenses:
            print("\n❌ No Expenses Found!")

        else:

            print("\n===== Expenses =====")

            print(
                f"{'ID':<5}"
                f"{'Date':<15}"
                f"{'Category':<15}"
                f"{'Amount':<10}"
                f"{'Description':<20}"
            )

            print("-" * 65)

            for expense in expenses:

                date = str(expense[1])[:10]

                print(
                    f"{expense[0]:<5}"
                    f"{date:<15}"
                    f"{expense[2]:<15}"
                    f"{expense[3]:<10}"
                    f"{expense[4]:<20}"
                )

    # ====================
    # Delete Expense
    # ====================

    elif choice == '3':

        expense_id = int(
            input("Enter Expense ID to Delete: ")
        )

        delete_expense(expense_id)

        print("\n🗑 Expense Deleted Successfully!")

    # ====================
    # Update Expense
    # ====================

    elif choice == '4':

        expense_id = int(
            input("Enter Expense ID: ")
        )

        category = input(
            "Enter New Category: "
        )

        amount = float(
            input("Enter New Amount: ")
        )

        description = input(
            "Enter New Description: "
        )

        update_expense(
            expense_id,
            category,
            amount,
            description
        )

        print("\n✏ Expense Updated Successfully!")

    # ====================
    # Exit
    # ====================

    elif choice == '5':

        category = input("Enter Category: ")
        amount = float(input("Enter Budget Amount: "))

        set_budget(category, amount)

        print("\n✅ Budget Set Successfully!")

    elif choice == '6':

        budgets = view_budgets()

        if not budgets:
            print("\n❌ No Budgets Found!")

        else:

            print("\n===== Budgets =====")

            print(
                f"{'Category':<20}"
                f"{'Budget Amount':<15}"
            )

            print("-" * 35)

            for budget in budgets:

                print(
                    f"{budget[1]:<20}"
                    f"{budget[2]:<15}"
                )

    elif choice == '7':
        category = input("Enter Category: ")
        check_budget(category)

    elif choice == '8':
        print("\n👋 Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("\n❌ Invalid Choice!")