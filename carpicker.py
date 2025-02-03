import random
print("Welcome to the car picker dialogue box")
cars = input("What type of car should I buy? Enter a list of cars seperated by comma and a space:\n")
randomised = cars.split(", ")
print(randomised)
randomised = random.choice(randomised)
print(f"Your choice car is {randomised}")
