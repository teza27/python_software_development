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

from typing import List
print(dir(List))