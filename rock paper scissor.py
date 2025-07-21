import random

choices = ['rock', 'paper', 'scissors']
while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif(user == 'rock' and computer == 'scissors') or \
        (user == 'scissors' and computer == 'paper') or \
        (user == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")
    play_again=input("Do you want to play again ...(yes\no) :")
    if play_again !="yes":
        print("thanks for playing game!!")
    break