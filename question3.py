#Grade Average Calculator
# Requirements:
# Create a function calculate_average(scores) that:
    # Takes a list of scores as a parameter
    # Calculates and returns the average
choice = int(input(f"How many test scores do you want to enter? "))
my_range = range(choice)
scores = []

for i in my_range:
    while True:
        try:
            num = int(input(f"Enter score {i+1}: "))
            scores.append(num)
            break
        except ValueError:
            print("Please enter a valid number")
print("\n")

def calculate_average(scores):
    average = sum(scores) / choice
    return average
grade_average = calculate_average(scores)

print("=== GRADE REPORT ===")
print(f"Test Scores: {scores}")
print(f"Average Score: {grade_average:.2f}")
# Create a function get_letter_grade(average) that:
    # Takes an average score as a parameter
    # Returns letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (below 60)
def get_letter_grade(scores):
    if grade_average >= 90: # FIXED? ===========================================================================
        return print("Letter Grade: A")
    elif 80 <= grade_average <= 89:
        return print("Letter Grade: B")
    elif 70 <= grade_average <= 79:
        return print("Letter Grade: C")
    elif 60 <= grade_average <= 69:
        return print("Letter Grade: D")
    else:
        return print("Letter Grade: F")
l_average = get_letter_grade(grade_average)

# Display the average and letter grade using your functions
# Use a while loop to:
    # Ask how many test scores to enter
    # Collect each score from the user
    # Store scores in a list