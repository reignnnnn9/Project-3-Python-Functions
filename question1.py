#Personal Budget 
# Requirements:
# Create a function called calculate_budget() that:
    # Asks the user for their monthly income
    # Asks for 3 expenses: rent, food, and entertainment
    # Calculates total expenses and remaining money
    # Uses if/elif/else to give budget advice:
        # If remaining money < 0: "You're overspending! Cut back on expenses."
        # If remaining money < 100: "Your budget is tight. Be careful with spending."
        # If remaining money >= 100: "Great job! You have money left over."

#QUESTIONS
# Displays a formatted summary === WHAT DOES THIS MEAN??
# Call the function at the end of your program === DOES IT HAVE TO BE AT THE END?
def calculate_budget(income, rent, food, entert):
    total_expenses = (rent + food + entert)
    remaining = income - total_expenses
    return total_expenses, remaining

income = float(input("Enter your montly income: $"))
rent = float(input("Enter rent expense: $"))
food = float(input("Enter food expense: $"))
entert = float(input("Enter entertainment expense: $"))

total_exp, remaining_bal = calculate_budget(income, rent, food, entert) #CALLING FUNCTION?
print("\n")

print("=== BUDGET SUMMARY ===")
print(f"Monthly Income: ${income:.2f}")
print(f"Total Expenses: ${total_exp:.2f}")
print(f"Remaining Money: ${remaining_bal:.2f}")
print("\n")

if remaining_bal < 0:
    print("Budget Advice: You're overspending! Cut back on expenses.")
elif remaining_bal < 100:
    print("Budget Advice: Your budget is tight. Be careful with spending.")
elif remaining_bal >= 100:
    print("Budget Advice: Great job! You have money left over.")