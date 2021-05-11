class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

# class Pet:
#     def __init__(self):
#         self.name = "Cujo"
#         self.fullness = 50
#         self.happiness = 20


class CuddlyPet(Pet): # This is a subclass. Pet is a parent class.
    pass

# cujo = Pet("Cujo", 50, 20)
# cujo.eat_food()
# print(cujo.fullness)
# # 80
# print(cujo, hapiness)
# # 50

# benji = Pet("Benji", 50, 100)
# print(benji.fullness)
# # 80
# print(benji.hapiness)
# # 80

benji = Pet("Benji", 50, 20, 20, 1)
lassie = Pet("Lassie", 50, 20, 20, 1)
clifford = Pet("Old Yeller", 50, 20, 20, 1)


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
