# OBJECT
class Cat:
    # Attribute! This is what all cats have. (Attributes, properties or states)
    species = "mammal"

    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describe(self):
        return "%s is %d years old" % (self.name, self.age)


guster = Cat("Guster", 11)
bandit = Cat("Bandit", 11)

print("%s is %d years old" % (guster.name, guster.age))
print("%s is %d years old" % (bandit.name, guster.age))
print("%s is a %s" % (guster.name, guster.species))
print("%s is %s's sister, they are both %s(s)" % (bandit.name, guster.name, guster.species))

# METHODS
print(guster.describe())
print(bandit.describe())

