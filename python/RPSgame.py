
# sorcery skip: merge-duplicate-blocks, remove-redundant-continue, remove-redundant-if
""" Rock paper scissor game in terminal window 
    hence the first begineer project
    SUCCESSFULLY DONE!!!!"""
import random

name = input("enter the name: ")
user_wins = 0
computer_wins = 0
draw = 0
n = 0
option = ["rock" , "paper" , "scissor"]
print("welcome to the game!",name)

while True:

    user_input = input("Enter the choices rock/paper/scissors/quit/q: ").lower()
    
    if (user_input == "q" or user_input == "quit"):
        break
    
    elif user_input not in option:
        print("guess the option given")
        
        
    
    
    random_number = random.randint(0,2)

    computer_guess = option[random_number]
    print("computer picked", computer_guess, ".")

    if (user_input == "rock"and computer_guess == "scissor" or
            user_input == "paper" and computer_guess == "rock"
        or user_input == "scissor"and computer_guess == "rock"):
        
        print("YOU WON!!!")
        user_wins += 1
        n += 1
        continue

    elif(user_input=="rock" and computer_guess=="rock" 
        or user_input == "paper"and computer_guess == "paper"
        or user_input == "scissor" and computer_guess == "scissor") :
        
        print(" Draw!!! ")
        draw +=1
        n += 1
        continue
        

    elif(user_input=="rock" and computer_guess=="paper" 
        or user_input == "paper"and computer_guess == "scissor"
        or user_input == "scissor" and computer_guess == "rock") :
        
        print("Computer wins !!!")
        computer_wins += 1
        n += 1
        continue


print("you won", user_wins , "times")
print("computer won", computer_wins , "times")
print("You had drawn", draw ,"times")
print("you played the game",n,"times")
print("Thank you for playing the game ")                   



