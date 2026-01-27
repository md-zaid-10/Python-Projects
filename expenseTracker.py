# Create a console-based Expense Tracker program in python that allows the user to record daily expenses and view summaries like total spending. 

# You are required to build  a simple personal dinanace management tool. Teh program should allow the user to:
    # Add an expense with the details like date, category, description and amount
    # View all recorded expenses in a clean format.
    # Calculate total spending so far.
    # Exit the program when the user chooses to.

# No user-defined funcitons or file handling should be used.


expenseList = [] # List of all expenses in form of dictionary

print("Welcome to Exprense Tracker!")

while True:
    print("====MENU====")
    print("Press 1 to Add Expense")
    print("Press 2 to View All Expense")
    print("Press 3 to View Total Expense")
    print("Press 4 to Exit")

    choice = int(input("Please Enter your choice: "))

# 1. Add expense
    if(choice == 1):
        date = input("what date did you spend? ")
        category = input("Type of Expense (food,travel, etc. )")
        description = input("Enter details of expense ")
        amount = float(input("Enter the total amount "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expenseList.append(expense)
        print("\n Expenses added Successfully. ")

# 2. View all expenses
    elif(choice == 2):
        if(len(expenseList) == 0):
            print("No expenses added. ")
        else:
            print("====These are all your expenses==== ")
            count = 1
            for eachExpense in expenseList:
                print(f"Expense Number {count} -> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]} ")
                count= count+1
    
# 3. View Total spending
    elif (choice == 3):
        total = 0
        for eachExpense in expenseList:
            total = total + eachExpense["amount"]

        print("\n Total Expense = ", total)

# 4. Exit
    elif(choice == 4):
        print("Thank you for using Expense Tracker")
        break

    else:
        print("Invalid Choice :( ")
        print("...Try Again...")