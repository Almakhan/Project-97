import random 
print("Number guessing game")
print("Guess a number (between 1 and 9)")
number = random.randint(1, 9)
chance=0

while chance < 5:
    guess=int( input("enter your guess:"))

    if guess == number:
        print("Congratulation YOU WON")
        break

    elif guess < number:
            print("Your guess was too low: Guess a number higher then", guess)

    else:
        print("Your guess was too high: Guess a number lower then", guess)

    chance += 1


if not chance < 5:
     print("YOU LOSE!! The number is", number)

        

