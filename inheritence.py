class human:                                       
    def __init__(self, name, age, gender):         

        self.name = name
        self.age = age 
        self.gender = gender

    def school(self):
        print(f"{self.name} is an {self.age} year old student who will be admitted in the {self.gender} section")

class player(human):
    def message(self):
        print(f"{self.name} is a {self.age} year old {self.gender} tennis player.")


a1= player("Serena Williams", 42, "Female")

a1.message()