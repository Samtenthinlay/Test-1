import random

secret_number = random.randint(1, 10)

max_attempts = 3

def welcome_message():
    print("\nwelcome to numder guessing game!")
    print(f"you have {max_attempts}")