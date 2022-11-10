'''
    Problem Statement: You have to write a Word Puzzle Game in which the user has to form
    the correct word out of a given set of characters. In the game the user has to solve this
    puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
    in random sequence. Give the user score +1 for each correct answer and give -1 for each
    wrong answer. At last print the final score. You can store any number of words in the list, but
    in each round of the game only 5 words are shown to the user.
'''
import random
import RandomWord_Generator
import UserInput
import CheckOut_Word

# Create a list of Word.
Word_List = ['apple', 'mango', 'andoid', 'iphone', 'windows', 'mac', 'linux', 'banana', "book", "pen", "vscode", "Python", "java", "mysql", "django"]

# Driver Code.
while True:

    # Create empty variable.
    UserScore = 0
    print()

    # Ask the user, Do you want to play Word Puzzle Game.
    print("Do you want to play Word Puzzle Game.")
    Yes_No = input("[y/n]>>> ").lower()
    if Yes_No!="y":
        print("Thank You! For using Python Word Puzzle Game.")
        break

    else:
        for i in range(5):
            
            # choose the random word from a Word_List.
            CW = random.choice(Word_List)

            # calling RandomWord_Generator function. ( From RandomWord_Generator Module).
            Shuffle_RandomWord = RandomWord_Generator.displayWord(CW)
            print("----------------------------------------------------------------")

            # calling User_Input function. ( From UserInput Module).
            userip = UserInput.User_Input(Shuffle_RandomWord,i+1)

            # calling CheckOut_Word function. ( From CheckOut_Word Module).
            FinalResult = (CheckOut_Word.CheckOut_Word(CW, userip))

            # final Scror clculation.
            if FinalResult:
                print("    Correct!")
                UserScore+=1
            else:
                print("    Wrong!")
                UserScore-=1

        else:
            print("----------------------------------------------------------------")
            print()
            print("Final Score is",UserScore)
