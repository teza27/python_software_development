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
"""
adding_value = lambda x, y : x + y
addition = adding_value(4, 5)
print(addition)

concat = lambda c, d : c + d
merge = concat("Temi", "tayo")
print(merge)
"""

"""
def discount_rate(rate_discounted: int):

    def total_cost():
        cart_list = input("Enter the price of each item bought, seperated by a comma and space\n")
        anew_cart = cart_list.split(", ")
        a_list_item = [int(i) for i in anew_cart]
        total = sum(a_list_item)
        return lambda : f"You have received a discount of {(total * rate_discounted) / 100:.2f} and your total payment due is {total - ((total * rate_discounted) / 100):.2f}"
    return total_cost
discount_rate = discount_rate(10)
print(discount_rate())
"""

"""
from functools import reduce
import re
def operations(operation_type, a, b):
    return operation_type(a, b)
multiply = lambda a, b : a * b

print(operations(multiply, 3, 6))

multiplication = multiply(4, 6)
print(multiplication)


sample_data = [200, 455.23, -306.5, 25000, -642.21, -133.9, 79.79, 1300, 5000, 3400, -150, -790, -3210, -1000, 8500, -30]

savings = sum(filter(lambda x : x != 0, list(map(lambda x : round(x * 0.05 if x > 0 else 0, 2), sample_data))))
print(f"Your total savings for the period is ${savings}")
# filtered_savings = sum(list(filter(lambda x : x != 0, savings)))
# print(filtered_savings)
# savings_formatted = f"{savings:.2f}"
# print(savings_formatted)
total_amount = reduce(lambda x, y : x + y, sample_data)
print(f"Total money you have received is ${total_amount}")

sales_data = [
    {"product": "Apple", "quantity": 5, "price": 2.5},
    {"product": "Banana", "quantity": 10, "price": 1.75},
    {"product": "Orange", "quantity": 8, "price": 3.0},
    {"product": "Grapes", "quantity": 3, "price": 4.25},
    {"product": "Mango", "quantity": 6, "price": 2.0},
]
filtered = reduce(lambda x, y : x + y, list(map(lambda sales: sales["quantity"] * sales["price"], list(filter(lambda data : data["product"] == "Grapes", sales_data)))))
print(filtered)

intro = "My name is Temitayo, A technical and cloud support engineer"

id = re.compile(r"a")

print(id.search(intro))
alphabet = re.compile(r"a", flags=re.IGNORECASE)
print(alphabet.findall(intro))
"""

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = [i for i in numbers if i % 2 == 0]
odd_num = [ i for i in numbers if i % 2 != 0]

print(numbers)
print(even_num)
print(odd_num)

user_details = {"name": "Temitayo", "class": "dept 2", "school": "school2"}

details = {key : value for key, value in user_details.items() if key == "name"}

print(details)
"""

"""
try:
    with open(r"new.txt", "r") as newfile:
        newfile.read()

except:
    with open (r"newest.txt", "w") as writefile:
        writefile.write("Here is a new file created and written to")

else:
    newfile.read()

finally:
    pass
    # with open(r"newest.txt", "r") as openfile:
    #     readup = openfile.read()
    #     print(readup)

with open(r"newest.txt", "r") as readafile:
    content = readafile.read()
    print(content)
"""

# Print sample student data

import json
student_data = {
    "student_id": "20231234",
    "first_name": "John",
    "last_name": "Doe",
    "age": 20,
    "gender": "Male",
    "department": "Computer Science",
    "institution": "XYZ University",
    "year_of_study": 3,
    "courses": [
        {"course_code": "CSC101", "course_name": "Introduction to Programming", "grade": "A"},
        {"course_code": "CSC203", "course_name": "Data Structures", "grade": "B+"},
        {"course_code": "MTH202", "course_name": "Calculus II", "grade": "A-"},
        {"course_code": "PHY105", "course_name": "General Physics", "grade": "B"}
    ],
    "GPA": 3.75,
    "email": "johndoe@xyzuniversity.edu",
    "phone": "+234-8012345678",
    "address": {
        "street": "123 University Road",
        "city": "Lagos",
        "state": "Lagos",
        "country": "Nigeria"
    },
    "scholarship": True,
    "hostel_resident": False,
    "date_of_birth": "2003-07-15"
}

# with open("data.json", "w") as textfile:
#     json.dump(obj=student_data, fp=textfile, indent=3)
# print(json.dumps(obj=student_data, indent=3))
# print(serialised_dict)

# deserialised_json = json.loads(serialised_dict)
# print(deserialised_json)

with open("student.json", "r") as student_info:
    student_bio = json.load(student_info)
    student_fname = student_bio["first_name"]
    student_lname = student_bio["last_name"] 
    student_bgrade = student_bio["courses"][0]["grade"]
    student_country= student_bio['address']["country"]
    print(f"{student_fname} {student_lname} best grade is {student_bgrade} and is from {student_country}")


with open(r"store_data.json", "r") as product:
    data = json.load(product)
    get_brand = data["store"]["departments"][0]["categories"][1]["products"][1]["brand"]
    get_name = data["store"]["departments"][0]["categories"][1]["products"][1]["name"]
    print(f"{get_brand} {get_name}")