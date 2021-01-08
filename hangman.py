import json
import random

with open('words.json') as file:
    print(random.choice(json.load(file).get("words")))