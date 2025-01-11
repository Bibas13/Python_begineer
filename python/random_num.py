"""Random number guess 
    second begineer level project 
    SUCCESSFULLY DONE!!!!"""
    
import random

rand = random.randint(1, 10)
print(rand)
guess_number =0

while True:
    
    user_int = int(input("Enter the number: "))
    

    if  (user_int > rand):
        print("Guess the lower number than this")
        guess_number += 1
        continue
    
    elif (rand > user_int) :
        print("Guess the number higher than this")
        guess_number += 1
        continue
    
    elif (user_int == rand) :
        print("you guessed the correct number")
        guess_number += 1
        break

print("you have guessd in ", guess_number, "times" )

    
    


    
    