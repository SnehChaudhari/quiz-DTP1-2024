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

# main routine
print()
print('Julian Dennison Quiz')
print()
print()

# loop (temporary)

want_instructions = yes_no('Would you like to read the instructions? ')

# checks want_instructions input
if want_instructions == 'yes':
    instructions()

print('...')