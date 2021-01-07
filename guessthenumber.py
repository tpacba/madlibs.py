import random


def guess(x):
    random_number = random.randint(0, x)
    guess = -1

    while guess != random_number:
        guess = int(input(f"Input your guess from 0 to {x}: "))
        if guess < random_number:
            print(f"{guess} is too low")
        if guess > random_number:
            print(f"{guess} is too high")
    
    print(f"{guess} is correct! Nice work!")

max = int(input("Range from 0 to __: "))

guess(max)