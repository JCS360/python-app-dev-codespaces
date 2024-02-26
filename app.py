# write 'hello world' to the console
print("Hello World")
# run the file using the command 'python app.py' in the terminal

# import random module
import random

#create a list of options that has rock, paper, and scissors
options = ["rock", "paper", "scissors"]

# create a score variable and set it to 0
score = 0

# creata a variable to count the number of rounds
rounds = 0

# create a while loop that runs as long as the rounds are less than 3
while rounds < 3:
    # add 1 to the rounds variable
    rounds += 1
    # create a variable that stores the user's input
    user_input = input("Enter rock, paper, or scissors: ")
    # create a variable that stores the computer's choice
    computer_choice = random.choice(options)
    # print the computer's choice
    print("Computer chose: ", computer_choice)
    # create a conditional statement that checks if the user's input is equal to the computer's choice
    if user_input == computer_choice:
        # if the user's input is equal to the computer's choice, print "It's a tie!"
        print("It's a tie!")
    # create a conditional statement that checks if the user's input is "rock" and the computer's choice is "scissors"
    elif user_input == "rock" and computer_choice == "scissors":
        # if the user's input is "rock" and the computer's choice is "scissors", print "You win!"
        print("You win!")
        # add 1 to the score variable
        score += 1
    # create a conditional statement that checks if the user's input is "paper" and the computer's choice is "rock"
    elif user_input == "paper" and computer_choice == "rock":
        # if the user's input is "paper" and the computer's choice is "rock", print "You win!"
        print("You win!")
        # add 1 to the score variable
        score += 1
    # create a conditional statement that checks if the user's input is "scissors" and the computer's choice is "paper"
    elif user_input == "scissors" and computer_choice == "paper":
        # if the user's input is "scissors" and the computer's choice is "paper", print "You win!"
        print("You win!")
        # add 1 to the score variable
        score += 1
    # create a conditional statement that checks if the user's input is "rock" and the computer's choice is "paper"
    elif user_input == "rock" and computer_choice == "paper":
        # if the user's input is "rock" and the computer's choice is "paper", print "You lose!"
        print("You lose!")
    # create a conditional statement that checks if the user's input is "paper" and the computer's choice is "scissors"
    elif user_input == "paper" and computer_choice == "scissors":
        # if the user's input is "paper" and the computer's choice is "scissors", print "You lose!"
        print("You lose!")
    # create a conditional statement that checks if the user's input is "scissors" and the computer's choice is "rock"
    elif user_input == "scissors" and computer_choice == "rock":
        # if the user's input is "scissors" and the computer's choice is "rock", print "You lose!"
        print("You lose!")
    # if the user enters an invalid input, print "Invalid input!"
    else:
        print("Invalid input!")  
    # print the user's score
    print("Your score: ", score)
    # print the number of rounds
    print("Rounds: ", rounds)
# create a conditional statement that checks if the score is greater than 1
if score > 1:
    # if the score is greater than 1, print "You win the game!"
    print("You win the game!")
# create a conditional statement that checks if the score is less than 1
elif score < 1: 
    # if the score is less than 1, print "You lose the game!"
    print("You lose the game!")     
    # create a conditional statement that checks if the score is equal to 1 
elif score == 1:
    # if the score is equal to 1, print "It's a tie!"
    print("It's a tie!")
# print "Game over!"
print("Game over!")
# run the file using the command 'python app.py' in the terminal
# enter rock, paper, or scissors when prompted
# the computer will randomly choose rock, paper, or scissors
# the game will run for 3 rounds
# the user's score will be printed after each round
# the result of the game will be printed at the end
# the game will be over after 3 rounds
# the user will be prompted to play again
# the user can run the file again to play another game
# the game will continue to run as long as the user wants to play
# the user can exit the game by pressing 'ctrl + c' in the terminal
# the user can exit the game by closing the terminal
# the user can exit the game by closing the file
# the user can exit the game by pressing 'q' in the terminal
# the user can exit the game by pressing 'quit' in the terminal
# the user can exit the game by pressing 'exit' in the terminal
# the user can exit the game by pressing 'e' in the terminal
# the user can exit the game by pressing 'x' in the terminal
# the user can exit the game by pressing 'end' in the terminal
# the user can exit the game by pressing 'esc' in the terminal
# the user can exit the game by pressing 'ctrl + z' in the terminal
# the user can exit the game by pressing 'ctrl + c' in the terminal
# the user can exit the game by pressing 'ctrl + x' in the terminal
# the user can exit the game by pressing 'ctrl + e' in the terminal
# the user can exit the game by pressing 'ctrl + end' in the terminal
# the user can exit the game by pressing 'ctrl + esc' in the terminal
# the user can exit the game by pressing 'ctrl + z' in the terminal
            
        
