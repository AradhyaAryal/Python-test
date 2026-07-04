secret = 3
i = 0
while i <= 5:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("You win")
        break
    else:
        print("You lose")
        i = i+1