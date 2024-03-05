#Mini python quiz game 

#A tuple of questions
questions = ("Brass gets discoloured in the air because of the presence of which of the following gases in air?", 
             "Which of the following is a non-metal that remains liquid at room temperature?", 
             "Chlorophyll is a naturally occurring chelate compound in which central metal is", 
             "Which of the following is used in pencils?", 
             "Which of the following metals forms an amalgam with other metals?")

#A tuple of options
options = (("A. Oxygen", "B. Hydrogen Sulphide", "C. Carbon Dioxide", "D. Nitrogen"), 
           ("A. Phosphorous", "B. Bromine", "C. Chlorine", "D. Helium"), 
           ("A. Copper", "B. Magnesium", "C. Iron", "D. Calcuim"),
           ("A. Graphite", "B. Silicon", "C. Charcol", "D. Phosphorous"),
           ("A. Tin", "B. Lead", "C. Mercury", "D. Zinc"))

#A tuple of correct answers
answers= ("B", "B", "B", "A", "B")

#A list of guesses
guesses = []    #We eill append guesses to a list. We canot append to a tupple, tuples are immutable

#Counting score of player
score = 0

#keeping track of question number
question_num = 0  

allowed_options = ("A", "B", "C", "D")

#Python handles the initialization, iteration, and termination of the loop internally, so you don't need to declare and initialize a loop control variable explicitly. The loop continues until it has iterated over all elements in the sequence.
#Iteratingo over tuple of questions
for question in questions:
    print("---------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess= input("Enter a choice (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------------------")
print("             RESULTS             ")
print("---------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)*100)
print(f"Your score is {score}%")