class human:                                       
    def __init__(self, name, age, gender):         

        self.name = name
        self.age = age 
        self.gender = gender

    def school(self):
        print(f"{self.name} is an {self.age} year old student who will be admitted in the {self.gender} section")


Rahim = human("Khan", 27 , "Male")

Rahim.school()