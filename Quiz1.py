#Author:Liu Yutong
#Date:04/06/25
# NUIST Quiz Game in Python
def quiz():
	print("Welcome to the Animal Quiz!")
	print("Answer the following questions:")

# Questions and Answers
questions = [
"1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat",
"2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird ",
"3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin "
]
answers = [
"Blue whale",
"Hummingbird",
"Bat"
]
score = 0

# Ask questions
for i in range(len(questions)):
	user_answer = input(questions[i]).strip().lower()
	if user_answer == answers[i].lower():
		print("Correct!")
		score += 1
	else:
		print("Incorrect!")

# Provide final score
print("\nQuiz completed!")
print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz finctoin
quiz()
