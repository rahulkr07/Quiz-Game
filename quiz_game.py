
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the capital of Jharkhand?",
        "options": ["A. Ranchi", "B. Dhanbad", "C. Bokaro Steel City", "D. Deoghar"],
        "answer": "A"
    },
    {
        "prompt": "Year Jharkhand became a state?",
        "options": ["A. 2001", "B. 2000", "C. 2003", "D. 1999"],
        "answer": "B"
    },
    
    {
        "prompt": "Most Pilgrim City'?",
        "options": ["A. Deoghar", "B.Dhanbad ", "C.BOKARO", "D. Jamshedpur"],
        "answer": "A"
    }
]

# Run the quiz
run_quiz(questions)
