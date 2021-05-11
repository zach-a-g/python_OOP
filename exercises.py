class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []

    def greet(self, other_person):
        self.greeting_count += 1
        if other_person.name not in self.unique_greeted:
            self.unique_greeted.append(other_person.name)
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        print("%s has greeted %d people" % (self.name, self.greeting_count))
        print("Number of unique people greeted is: %s" % len(self.unique_greeted))

    def print_contact_info(self):
        print("Name: %s, Email: %s, Phone: %s" % (self.name, self.email, self.phone))
    
    def add_friends(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print(len(self.friends))
    
    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)

    def num_unique_greeted(self):
        # uniques = set(self.unique_greeted)
        # uniques_greeted = list(uniques)
        print("The number of unique people greeted is: %d" % (len(self.unique_greeted)))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
dee_ann = Person("Dee ann", "deeann@aim.com", "123-456-7890")

# Create a Vehicle class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
   
    def print_info(self):
        print(car.make, car.model, car.year)

car = Vehicle("Ram", "1500", "2020")

car.print_info()
print("====================")

# Printing contact info through class variable strings
print(sonny.__str__())
print("%s's contact info is: %s, %s ." % (sonny.name, sonny.email, sonny.phone))
print("%s's contact info is: %s, %s ." % (jordan.name, jordan.email, jordan.phone))

# Print contact info with def function
sonny.print_contact_info()

# Counting friends
print(len(jordan.friends))
jordan.add_friends(sonny)
sonny.add_friends(jordan)
jordan.num_friends() # This goes from 0 to 1 because I added a friend in line 51.
print("====================")

# Counting how many people self has greeted
print("Sonny has greeted this many people: " + str(sonny.greeting_count))
print("")
print(sonny.greet(jordan))
print("Sonny has now greeted: " + str(sonny.greeting_count)) 
print("")
print(sonny.greet(jordan))
print(sonny.greeting_count)

# Converting object to string (__str__)
print(jordan)
print("====================")

# Bonus
# Keep track of number of unique people greeted
sonny.num_unique_greeted()
sonny.greet(jordan)
sonny.num_unique_greeted()
sonny.greet(jordan)
sonny.num_unique_greeted()
sonny.greet(dee_ann)
sonny.num_unique_greeted()
print("====================")

