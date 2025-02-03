fullcardnum = input("Enter your full card number\n")
# print(fullcardnum)
# print(type(fullcardnum))
masked_pan = []
for char in fullcardnum:
    if char == " ":
        pass
    elif len(masked_pan) < 12:
        new_char = char.replace(char, "*")
        masked_pan.append(new_char)
    else:
        masked_pan.append(char)
new_masked = "".join(masked_pan)
print(new_masked)
# print(type(new_masked))