questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language are we using for this quiz?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "A"
    },
    {
        "question": "What is 5 × 6?",
        "options": ["20", "25", "30", "35"],
        "answer": "C"
    }
]

score = 0

print("===== PYTHON MCQ QUIZ =====")

for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    for i, option in enumerate(question["options"]):
        print(f"{chr(65 + i)}. {option}")

    answer = input("Your answer: ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== QUIZ FINISHED =====")
print(f"Your score: {score}/{len(questions)}")
