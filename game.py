secret_number = 69
attempts = 3

while attempts > 0:
    guess = int(input("Guess the secret number: "))
    
    if guess == secret_number:
        print("You got it! The secret number was 69!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong! Try again. You have {attempts} attempts left.")
        else:
            print("haha you a loser try again")

