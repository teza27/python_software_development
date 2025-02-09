class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I work as a {self.occupation}")
    def change_occupation(self, new_occupation):
        self.occupation = new_occupation
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I work as a {self.occupation}")

temitayo = Person("temitayo", 27, "Cloud Engineer")
temitayo.introduce()
temitayo.change_occupation("Python Developer")
print(temitayo.occupation)
