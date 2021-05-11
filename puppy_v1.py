# Define a dictionary that holds our pet's attributes.

# Define multiple dictionaries that holds each pet's attributes.
puppy_1 = {
    "name": "Cujo",
    "fullness": 50,
    "happiness": 20,
    "hunger" : 7,
    "mopiness": 4,
}

puppy_2 = {
    "name": "Benji",
    "fullness": 50,
    "happiness": 100,
    "hunger": 3,
    "mopiness": 2,
}

# Each pet is adjusted invidually.
def get_hungry_and_mopey(pet):
    pet["fullness"] -= pet["hunger"]
    pet["happiness"] -= pet["mopiness"]

# Define a list that holds all of our pets.
pets = [puppy_1, puppy_2]

# Define functions that increase a pet's attribute levels.
def feed_pet(pet):
    pet["fullness"] += 10

def play_with_pet(pet):
    pet["happiness"] += 10

# Decrease a pet's attribute levels.    
def get_hungry_and_mopey(pet):
    pet["fullness"] -= 5
    pet["happiness"] -= 5

# Prompt the user to interact with the pet
while True:

    # Loop through each pet, printing their status
    print("""
%s's stats:
Fullness: %d
Happiness: %d
""" % (pet["name"], pet["fullness"], pet["happiness"]))
    
    choice = int(input("""
1. Feed puppy
2. Play with puppy
3. Do nothing
"""))
    if choice == 1:
        which_pet = int(input("Which pet? "))
        feed_pet(pets[which_pet])
    elif choice == 2:
        which_pet = int(input("Which pet? "))
        play_with_pet(pets[which_pet])
    else:
        pass

    # Each time the loop runs, the pet
    # will need some attention!
    for pet in pets:
        get_hungry_and_mopey(pet)

