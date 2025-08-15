# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module.
def max(a,b):
    if a>b:
        return b
    else:
        return a

max_score =0
while(1):
    print("\n --------------------------------------------------------------------------------------------\n")
    print("______Welcome to the number guessing game______\n")
    print("Rules:\n1. I will generate a random number between 1 and 100.\n2. You have to guess the number.\n3. If your guess is too high, I will tell you to guess lower.\n4. If your guess is too low, I will tell you to guess higher.\n5. When you guess the correct number, I will tell you how many guesses it took you.\n6. You can exit the game by entering 0.\n")
    import random
    count=0
    number = random.randint(1,10)
    guess = int(input("Enter your guess: "))
    
    if guess<0 or guess>10:
        print("Invalid input. Please enter a number between 1 to 100.")
        continue
    elif guess == 0:
        print("Exiting the game. Thank you for playing!")
        break
    else:
        count+=1
        while guess != number:
            if guess<number:
                print("Higher number please")
                count+=1
                guess = int(input("Enter your guess: "))
            else:
                print("Lower number please")
                count+=1
                guess = int(input("Enter your guess: "))    
        else:
            if max_score ==0:
                max_score = count
            else:
                max_score = max(max_score, count)
            print("Yes you Guessed right and your score is: ",count)
            print("Your highest score is: ",max_score)

        
