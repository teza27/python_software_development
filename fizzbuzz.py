print("This exercise checks if the inputed number is divisible by 3, 5 or both.")
enter = input("Enter as many digits as you want, separated by comma and a space:\n")
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