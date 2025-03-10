import random
playing=True
number=str(random.randint(10,20))
print("i wll generate a number from 10 to 20, and you have to guess the number one digit ata time.")
print("the game ends when you get 1 hero")
while playing:
    guess=input("give me your best guess! \n")
    if number ==guess:
        print("you win the game")
        print("the number was", number)
        break
    else:
        print("your guess isnt quite right, try again. \n")
