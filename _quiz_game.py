import time
while True:
    score = 0
    total_question = 5
    print("Loading quiz...Please wait for a few seconds!")
    time.sleep(3)
    name = input("Enter your name: ")
    print("Welcome to the computer quiz!",name)
    playing = input("Do you want to play? ").lower()
    if playing != "yes":
        quit()
    print("Kay Cool! Lets play then!")

    questions = [
        {
            "question":"1. Who developed Python?: ",
            "options":["A)Guido van rossum", "B)Elon Musk", "C)David Goggins","D)Varun Dhavan"],
            "answer": "A"
        },
        {
            "question":"2. What is the file extension of Python files?: ",
            "options":["A)python()", "B).python", "C).py","D).pyp"],
            "answer": "C"
        },
        {
            "question":"3. Which function is used to display output in Python? ",
            "options":["A)input()", "B)output()", "C)terminal()","D)print()"],
            "answer": "D"
        },
        {
            "question":"4. Which symbol is used for comments in Python?: ",
            "options":["A)@", "B)#", "C)$","D)*"],
            "answer": "B"
        },
        {
            "question":"5. Which keyword is used to define a function in Python?: ",
            "options":["A)func", "B)key", "C)word","D)def"],
            "answer": "D"
        }
    ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer: ").upper()
        if user_answer==q["answer"]:
            print("Correct!")
            score +=1
        else:
            print("Incorrect! The correct answer is",q["answer"])
    
    print("Quiz Finished! ")
    print("You solved " + str(score) + " question's correctly")
    print("You got " + str((score/total_question)*100) + "%")
    if score == total_question:
        print("Excellent! You got a perfect score.")
    elif score >= 0.6*total_question:
        print("You got a good score.")
    else:
        print("Keep Learning Python!")

    replay = input("Do you want to play this game again(yes/no): ").lower()

    if replay != "yes":
        print("Thanks for playing!")
        break