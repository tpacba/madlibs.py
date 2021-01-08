import random

win = False

while win == False:
    comp = random.choice(["r", "p", "s"])
    user = input("Type (r) for rock, (s) for scissors, (p) for paper: ")

    print(f"Computer: {comp} \nUser: {user}")

    if user == comp:
        print("Tie!")
    elif (user == "r" and comp == "s") or (user == "s" and comp == "p") or (user == "p" and comp == "r"):
        print("Win!")
        win = True
    else:
        print("Lose!")
