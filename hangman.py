import json
import random
import string

def get_random_word():
    with open('words.json') as file:
        random_word = random.choice(json.load(file).get("words"))
        return random_word

def hangman():
    word = get_random_word()
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(used_letters))
        print(f"You have {lives} left")

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Correct! \n")
            else:
                lives -= 1
                print("Letter not in word! \n")
        elif guess in used_letters:
            print("Letter already used! \n")
        else:
            lives -= 1
            print("Letter not in word! \n")
    
    if lives == 0:
        print(f"Lost! The word was {word}.")
    else: 
        print(f"Win! The word was {word}.")

hangman()