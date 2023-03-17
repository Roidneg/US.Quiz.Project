#This is a simple basic US history theme 5 question quiz game 



print("Welcome to your quiz game!")

playing = input("Do you want to play a history game? ")

if playing.lower() != "yes":
    quit()
print ("Okay! Let's have fun")
#Now here i will be adding a scoring element to keep track of the players score.
score = 0
#1 My first question. Very simple and straight forward
answer = input("Who was the first President of the United States? ")
if answer == "George Washington":
    print("Correct! George Washington was the first President of the United States. Well done!")
    score += 1
else:
    print("Sorry, incorrect!")
    
#2 My second question. A bit more complex, but mostly a rehash of the first.
answer = input("How many orginal colonies were there? ")
if answer == "13":
    print("Correct! There were 13 orginal colonies. Well done!")
    score += 1
else:
    print("Sorry, incorrect!")

#3 My first complex questions in terms of multiple anwers.
question = "What was a name one of the original colonies? "
possible_answers = ["Virginia", "Massachusetts", "New Hampshire", "Maryland", "Connecticut", "Rhode Island", "Delaware", "North Carolina", "South Carolina", "New Jersey", "New York", "Pennsylvania", "Georgia"]

#Prompt the user for their response
answer = input(question)

#Check if the response matches any of the possible answers
if answer in possible_answers:
    print("Correct! Well done!")
    score += 1
else:
    print("Sorry, that's not one of the original colonies.")


#4 In this next question. I want to know expand on the first example code but make it case-insensitive as often people will write the correct answer but forget to use proper capitalization.
#Define the correct answer
correct_answer = "John Adams"

question = input("Who was the second President of the United States? ")
#So I will be using the title method to convert the users answers just in case if they don't.
question = question.title()
if question == correct_answer:
    print("Correct! Well done!")
    score += 1
else:
    print("Sorry, incorrect!")


#5 Same idea of question 4 but a different question
#Define the correct answer
correct_answer = "Joe Biden"

question = input("Who is the current President of the United States? ")
#So I will be using the title method to convert the users answers just in case if they don't.
question = question.title()
if question == correct_answer:
    print("Correct! Well done!")
    score += 1
else:
    print("Sorry, incorrect!")
#I wanted to add something extra at the end.
print("You got " + str(score) + " questions correct!")
if score == 5:
    print("You're a history wizard!")
