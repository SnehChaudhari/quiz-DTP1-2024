# point to add to the score
POINT = 1

# Function to prompt user for a yes/no answer
def yes_no(question):
    while True:
        response = input(question).lower()

        # Check the answer given
        # Repeat if invalid input (not y/n)
        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please enter a yes or no answer.')


# Function to print instructions for the quiz
def instructions():
    print('''
    ------ Instructions ------

    You will be asked various types of questions about Julian Dennison.
    These include multichoice, true or false, and answer required questions.
    Your score and level will be displayed as Score and Question.

    If you answer correctly, you will get one point to your score.
    If you get the question wrong, you won't get any points.

    Your knowledge about Julian Dennison will be displayed at the end of 
    the quiz as a percentage of knowledge.

    Good Luck!
    ''')


# Function to ask a question and check if the answer is correct
def ask_question(question):
    print(question['text'])
    if 'options' in question:
        for option in question['options']:
            print(option)
        expected_answers = ['a', 'b', 'c', 'd']
    elif 'correct_answer' in question and (question['correct_answer'] == 'true'
                                           or question['correct_answer']
                                           == 'false'):
        expected_answers = ['true', 'false']
    else:
        expected_answers = []

    # loop so that the question repeats when an invalid answer is given
    while True:

        # .strip().lower() removes any spaces and converts the answer to lowercase
        # bonus feature to make the program efficient
        answer = input('Enter your answer: ').strip().lower()

        # Check if the user wants to quit
        if answer == 'quit':
            return 'quit'

        # check if the answer is expected and gives the user feedback
        # on how to answer the question correctly
        if expected_answers and answer not in expected_answers:
            if expected_answers == ['a', 'b', 'c', 'd']:
                print('Please answer the question as a, b, c, or d.')
            elif expected_answers == ['true', 'false']:
                print('Please answer the question as true or false.')
        else:
            # Return whether the answer is correct
            return answer == question['correct_answer']


# Function to return a list of quiz questions
def get_questions():
    return [{
        "text":
        "1. In which country was Julian Dennison born?",
        "options":
        ["a) Australia", "b) New Zealand", "c) United States", "d) Canada"],
        "correct_answer":
        "b"
    }, {
        "text":
        "2. What is the name of the 2016 film in which Julian Dennison starred as Ricky Baker?",
        "options": [
            "a) Hunt for the Wilderpeople", "b) The Dead Lands", "c) Boy",
            "d) What We Do in the Shadows"
        ],
        "correct_answer":
        "a"
    }, {
        "text":
        "3. Which character did Julian Dennison portray in the movie 'Deadpool 2'?",
        "options": [
            "a) Cable", "b) Russell Collins / Firefist", "c) Domino",
            "d) Negasonic Teenage Warhead"
        ],
        "correct_answer":
        "b"
    }, {
        "text": "4. What is Julian Dennison’s middle name?",
        "options": ["a) Alistair", "b) James", "c) Bailey", "d) Richard"],
        "correct_answer": "c"
    }, {
        "text":
        "5. Julian Dennison won the New Zealand Film Award for Best Supporting Actor for his role in 'Shopping'.",
        "correct_answer": "true"
    }, {
        "text": "6. Julian Dennison was born in 2002.",
        "correct_answer": "true"
    }, {
        "text":
        "7. Julian Dennison played a role in the movie 'Godzilla vs. Kong'.",
        "correct_answer": "true"
    }, {
        "text": "8. In which year did Julian Dennison make his film debut?",
        "correct_answer": "2013"
    }, {
        "text":
        "9. Name the director of the film 'Hunt for the Wilderpeople'.",
        "correct_answer": "taika waititi"
    }, {
        "text":
        "10. What is the title of the short film that marked Julian Dennison’s debut?",
        "correct_answer": "shopping"
    }]


# Main routine of the quiz
def main():
    print('Julian Dennison Quiz\n')

    # Ask the user if they want to read the instructions
    want_instructions = yes_no('Would you like to read the instructions? ')

    # Check want_instructions input and display instructions if needed
    if want_instructions == 'yes':
        instructions()

    # Initialize the score
    score = 0

    # Get the list of questions
    questions = get_questions()

    # Get the total number of questions
    total_questions = len(questions)

    # Loop through each question
    for question in questions:
        result = ask_question(question)

        # Check if the user wants to quit
        if result == 'quit':
            break

        # Update the score based on the result
        elif result:
            print("Correct!")
            score += POINT
        else:
            print("Incorrect.")
        print()

    # calculates percentage based on total score and questions
    percentage = (score / total_questions) * 100

    # determines the grade the user got based on score
    if score > 9:
        grade = 'perfect'
    elif score > 8:
        grade = 'a pro'
    elif score > 6:
        grade = 'good'
    elif score > 4:
        grade = 'average'
    elif score > 2:
        grade = 'bad'
    else:
        grade = 'horrible'

    # Display the final score and percentage
    print(f'Your final score of this quiz is {score}/{total_questions}.')
    # calculates percentage based on total score and questions
    percentage = (score / total_questions) * 100
    print(f'Your knowledge about Julian Dennison is {percentage}%.')
    # displays the grade the user got based on grade
    print(f'This means that you are {grade} at this quiz.')
    print('Thanks for playing!')


# calls the main function to run the code
main()
