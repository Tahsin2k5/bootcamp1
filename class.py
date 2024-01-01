class human:                                         #Classes
    def __init__(self, name, age, gender):           #Constructor   ----- #attributes   

        self.name = name
        self.age = age 
        self.gender = gender

thing1 = human("Tahsin Ahmed", 18, "Male")            #Instance / #object

print(thing1.gender)
print(thing1.name)
print(thing1.age)
