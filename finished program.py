# asks the user if they want the instructions
def yes_no(question):
    while True:
        response = input(question).lower()

          # checks the answer given
          # repeats if invalid input (not y/n)
        if response == 'yes' or response == 'y':
              return 'yes'
        elif response == 'no' or response == 'n':
             return 'no'
        else:
            print('Please enter a yes or no answer.')



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


# asking the questions function
def ask_question(question):
    print(question['text'])
    if 'options' in question:
        for option in question['options']:
          print(option)
    answer = input('Enter your answer: ').strip().lower()
    if answer == 'quit':
        return 'quit'
    return answer == question['correct_answer']

# questions (as a list) function
def get_questions():
    return [
        {
            "text": "1. In which country was Julian Dennison born?",
            "options": ["a) Australia", "b) New Zealand", "c) United States", "d) Canada"],
            "correct_answer": "b"
        },
        {
            "text": "2. What is the name of the 2016 film in which Julian Dennison starred as Ricky Baker?",
            "options": ["a) Hunt for the Wilderpeople", "b) The Dead Lands", "c) Boy", "d) What We Do in the Shadows"],
            "correct_answer": "a"
        },
        {
            "text": "3. Which character did Julian Dennison portray in the movie 'Deadpool 2'?",
            "options": ["a) Cable", "b) Russell Collins / Firefist", "c) Domino", "d) Negasonic Teenage Warhead"],
            "correct_answer": "b"
        },
        {
            "text": "4. What is Julian Dennison’s middle name?",
            "options": ["a) Alistair", "b) James", "c) Bailey", "d) Richard"],
            "correct_answer": "c"
        },
        {
            "text": "5. Julian Dennison won the New Zealand Film Award for Best Supporting Actor for his role in 'Shopping'.",
            "correct_answer": "true"
        },
        {
            "text": "6. Julian Dennison was born in 2002.",
            "correct_answer": "true"
        },
        {
            "text": "7. Julian Dennison played a role in the movie 'Godzilla vs. Kong'.",
            "correct_answer": "true"
        },
        {
            "text": "8. In which year did Julian Dennison make his film debut?",
            "correct_answer": "2013"
        },
        {
            "text": "9. Name the director of the film 'Hunt for the Wilderpeople'.",
            "correct_answer": "taika waititi"
        },
        {
            "text": "10. What is the title of the short film that marked Julian Dennison’s debut?",
            "correct_answer": "shopping"
        }
    ]

    # main routine
def main():
    print('Julian Dennison Quiz\n')

    # asks the user if they want to read the instructions
    want_instructions = yes_no('Would you like to read the instructions? ')
    # checks want_instructions input
    if want_instructions == 'yes':
        instructions()

    score = 0
    questions = get_questions()
    total_questions = len(questions)

    for question in questions:
        result = ask_question(question)
        if result == 'quit':
            break
        elif result:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        print()
        
    print(f'Your final score of this quiz is {score}/{total_questions}.')
    percentage = (score / total_questions) * 100
    print(f'Your knowledge about Julian Dennison is {percentage}%.')
    print('Thanks for playing!')


if __name__ == "__main__":
    main()
