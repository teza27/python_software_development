terms = input("Enter as many numbers as you want seperated by comma and a space:\n")
new = terms.split(", ")
mean_calc = []
for num in new:
    convert = int(num)
    mean_calc.append(convert)
    mean = sum(mean_calc) / len(mean_calc)
print(mean)