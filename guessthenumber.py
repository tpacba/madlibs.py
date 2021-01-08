import random
import inquirer

# def guess(x):
#     random_number = random.randint(0, x)
#     guess = -1

#     while guess != random_number:
#         guess = int(input(f"Input your guess from 0 to {x}: "))
#         if guess < random_number:
#             print(f"{guess} is too low")
#         if guess > random_number:
#             print(f"{guess} is too high")
    
#     print(f"{guess} is correct! Nice work!")

# max = int(input("Range from 0 to __: "))

# guess(max)

def computer_guess(x):
    low = 0
    high = x
    correct_guess = False
    count = 0

    while correct_guess == False:
        random_number = random.randint(low,high)
        count += 1

        print(f"Attempt #{count}")
        print(f"Is the number {random_number}?")

        answer = inquirer.prompt([
            inquirer.List(
                "answer",
                message="Is the number too low, too high, or correct?",
                choices=["Too Low", "Too High", "Correct"]
            )
        ])

        if answer.get("answer") == "Too Low":
            low = random_number + 1
        elif answer.get("answer") == "Too High":
            high = random_number - 1
        elif answer.get("answer") == "Correct":
            correct_guess = True

    print(f"Nice work! It took {count} guesses.")


max = int(input("Give a range, 0 to ___: "))
enter = input(f"Think of a number from 1 to {max} and I'll guess it. \n (Press Enter to start.)")
computer_guess(max)