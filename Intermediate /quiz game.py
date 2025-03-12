questions = (
    "How many elements are in the periodic table?: ",
    "Which animal is the biggest?: ",
    "What is the most abundant resource in the atmosphere?: "
)


options = (
    ("A. 100", "B. 200", "C. 118", "D. 150"),
    ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Colossal Squid"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen")
)


answers = ("C", "B", "A")

guesses = []
score = 0


for question_num, question in enumerate(questions):
    print("--------")
    print(question)


    for option in options[question_num]:
        print(option)


    guess = input("Enter your guess (A, B, C, or D): ").strip().upper()
    guesses.append(guess)


    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[question_num]}")

print("---------")
print(" RESULTS ")
print("---------")

# Display correct answers
print("Correct answers:", end=" ")
for answer in answers:
    print(answer, end=" ")

print("\nYour guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")

print()

# Calculate and display final score
score_percentage = int((score / len(questions)) * 100)
print(f"Your final score is {score_percentage}%")
