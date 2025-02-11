# import module
# from module import *
# #print(all_customer())

# add_new("Anjie Mimiokan", 4)
# print(detailed_list())
# #newness = module.add_new("Adepega McAuthur", 4)
# #print(newness)
# print((module))
"""
import random
#'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
# 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular',
# 'uniform', 'vonmisesvariate', 'weibullvariate'
scores = [67, 98, 49, 76, 88, 98]
#print(dir(random))
#uniform = random.uniform(scores)
#random.seed(4)
# random.shuffle(scores)
# print(scores)

random_num = random.randint(40, 100)
print(random_num)
"""
# number = []
# for num in range(1, 5):
#     number.append(num)
# print(number)
# print(number[2])
# print(dir(number))
# others = ['jump', 'set']
# number_dir = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort', 'index']
# print(len(number_dir))
# print(number_dir[-1])
# number_dir[-1] = "remove"
# print(number_dir)
# print(number_dir.index("reverse"))
# print(number_dir.reverse())
# print(number_dir.sort())
# print(number_dir.append("newest"))
# print(number_dir.count("index"))
# print(number_dir.extend(others))
# print(number_dir.pop(-1))
# adding = number_dir.insert(-1, "multiply")
# print(number_dir)
# print(number_dir.copy())
# print(number_dir.clear())

# bb_alltime_great = ("Lebron", "Kobe", "Jordan", "Durant", "Curry", "Rajon")
# first, second, third, *fourth = bb_alltime_great
# converted = [first, second, third, *fourth]
# #print(bb_alltime_great)
# print(converted)
# print(fourth)

# database = set()
# database.add("temitayo")
# database.add("david")
# database.add("temitayo")
# print(database)

"""
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
enter = (input("Enter as many digits as you wanted, separated by comma and a space:\n"))
conver = enter.split(", ")
for digit in conver:
    new = int(digit)
    if new % 3 == 0 and new % 5 == 0:
        print("fizzbuzz")
    elif new % 3 == 0:
        print("fizz")
    elif new % 5 == 0:
        print("buzz")
    else:
        print(new)
"""
"""
terms = input("Enter as many numbers as you want seperated by comma and a space:\n")
new = terms.split(", ")
mean_calc = []
for num in new:
    convert = int(num)
    mean_calc.append(convert)
    mean = sum(mean_calc) / len(mean_calc)
print(mean)
"""

"""
import pdb
def sumfig(a, b):
    #pdb.set_trace()
    result = a + b
    #print(result)
    return result
sumfig(2, 4)
"""
"""
def customer_order():
    temitayo = "rice"
    adeolu = "beans"
    mike = "pizza"
    beatrice = "bugger"

    number_of_order = 2 * 4
    order_list = [temitayo, adeolu, mike, beatrice]
    return number_of_order, order_list
list_name = (customer_order())
count, order = list_name
print(count)
print(order)
convert_to_list = [count, order]
print(convert_to_list)
"""
"""
bank_customer_bal = {}
bank_customer_bal["Temitayo"] = 30000
bank_customer_bal["Adeolu"] = 15000

print(bank_customer_bal)
print(bank_customer_bal["Adeolu"])
"""

state_capital = {
    "Lagos": "Ikeja",
    "Oyo": "Ibadan",
    "Kogi": "Lokoja",
    "Ogun": "Abeokuta"
}

"""
print(state_capital)

for state, capital in state_capital.items():
    print(state,":", capital)

for state in state_capital.values():
    name = state.
    print(state)

#print(state_capital.)

def veggies(veggies_name):

"""

"""
fruit_categories = {
    'fruit': {
        'apple': {
            'color': 'red',
            'taste': 'sweet'
        },
        'banana': {
            'color': 'yellow',
            'taste': 'sweet'
        }
    },
    'vegetable': {
        'carrot': {
            'color': 'orange',
            'taste': 'crunchy'
        },
        'spinach': {
            'color': 'green',
            'taste': 'bitter'
        }
    }
}


def vitamins(category: str, values: dict):
    for key, value in values.items():
        for fruit, features in value.items():
            if fruit == category:
                color = features.get("color")
                taste = features.get("taste")
                print(f"{fruit} is a {key}, it is {color} in colour and has {taste} taste")

vitamins("apple", fruit_categories)
"""

"""
category_1 = {"student1": 200, "student2": 350, "student3": 400}
category_2 = {"teacher1": 600, "teacher2": 900, "teacher3": 700}
category_1.update(category_2)
print(category_1)

category_3 = {**category_1, **category_2}
print(category_3)
"""

"""
def attendees_name(**names):
    for key, value in names.items():
        print("Hello,", key,":", value)

attendees_name(name="temitayo", age=20, gender= "male")
"""

"""
statement = "The Lord of host is a good Lord , The Lord is mighty in deed"
def word_count(statement, *args):
    state_split = statement.split()
    print(state_split)
    word_dict = {}
    for char in args:
        word_number = state_split.count(char)
        word_dict[char] = word_number
    print(word_dict)
word_count(statement, "Lord", "host", "mighty", "deed", "The", "is")
"""

"""
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
"""

"""
class Animal():
    # Base class or Parent class or Super class
    def __init__(self):
        pass
    def breath():
        print("Animal can breath")
    def growth():
        print("Animal can grow")
class AquaticAnimal(Animal):
    # sub class or child class or derived class
    def __init__(self):
        pass
    def swim():
        print("Aquatic animal can swim")

fish = AquaticAnimal
fish.breath()
fish.growth()
fish.swim()
"""

"""
class Vehicles:
    def __init__(self, manufacturer: str, model: str, year: int):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
    def get_details(self):
        print(f"{self.manufacturer} {self.model} {self.year} model")

class Car(Vehicles):
    def __init__(self, manufacturer: str, model: str, year: int, num_door: int):
        super().__init__(manufacturer, model, year)
        self.num_door = num_door
    def get_details(self):
        print(f"The automobile {self.model} is made by {self.manufacturer} in the year {self.year} and has {self.num_door} doors")

class Motorcycle(Vehicles):
    def __init__(self, manufacturer: str, model: str, year: int, top_speed: float):
        super().__init__(manufacturer, model, year)
        self.top_speed = top_speed
    def get_details(self):
        print(f"The automobile {self.model} is made by {self.manufacturer} in the year {self.year} and a top speed of {self.top_speed}")
        

class Truck(Car):
    def __init__(self, manufacturer: str, model: str, year: int, num_door, cargo_capacity: float):
        super().__init__(manufacturer, model, year, num_door)
        self.cargo_capacity = cargo_capacity
    def get_details(self):
        print(f"The automobile {self.model} is made by {self.manufacturer} in the year {self.year} and has {self.num_door} doors and cargo capacity of {self.cargo_capacity}")
        
    
sedan_car = Car("Toyota", "Corolla", 2013, 4)
sedan_car.get_details()

power_bike = Motorcycle("BMW", "GT", 2013, "350MPH")
power_bike.get_details()

excation_truck = Truck("CAT", "Howo", 2010, 2, 40.5)
excation_truck.get_details()
"""

# view = open(file="C:/Users/TEMITAYO-OLAIYA/OneDrive - systemspecs.com.ng/PAPSS/PAPSS Infrastructure Items/reporting module error.txt", mode="r")
# print(view.read())

# with open("C:/Users/TEMITAYO-OLAIYA/OneDrive - systemspecs.com.ng/PAPSS/PAPSS Infrastructure Items/reporting module error.txt","r") as newest:
#     print(newest.read())


# with open("new text.txt", "x"):
#     pass
"""
with open("new text.txt", "w") as text_edit:
   text_edit.write("Testing hwo to add content to existing blank doc")
#print(text_edit())
"""

import csv
# file = open("new text.txt","r")
# print(file.read())

# with open("new text.txt", "r") as new_file:
#     print(new_file.read())
#     #print(new_file)


"""
with open("Updated file.txt", "r") as updated_file:
    print(updated_file.readlines())

students = [
    ["Name", "Age", "Class"],
    ["Temitayo", 12, "Class 2"],
    ["Adeolu", 19, "Class 4"],
    ["Omot", 8, "Class 1"]
]

with open("student.csv", "w") as student_list:
    writer = csv.writer(student_list)
    writer.writerows(students)


nigeria_data = [
    ["State", "Capital", "Tribe"],
    ["Lagos", "Ikeja", "Yoruba"],
    ["Rivers", "Port Harcout", "Igbo"],
    ["Jigawa", "Dutse", "Hausa"]
]

with open("state.csv", "w") as state_info:
    nig = csv.writer(state_info)
    nig.writerows(nigeria_data)

with open("state.csv", "r") as read_state_info:
    readFile = csv.reader(read_state_info)
    for item in readFile:
        print(item)
"""

adding_value = lambda x, y : x + y
addition = adding_value(4, 5)
print(addition)

concat = lambda c, d : c + d
merge = concat("Temi", "tayo")
print(merge)