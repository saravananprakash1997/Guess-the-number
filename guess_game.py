# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
number = random.randint(1,9)
name=input("Enter your name:")
print("Welcome "+str(name)+", let us get into the game")
for i in range(10):
    if i==3:
        print("\n Ran out of attempts","sorry u have lost")
        print("The guessed number is "+str(number))
        break
    guessed=int(input("Enter what you have guessed"+"(attempt no."+str(i+1)+"): "))
    
    if guessed ==number:
        print("You have founded in "+str(i+1)+" attempts")
        break
    else:
        print('What you have guessed is wrong')
