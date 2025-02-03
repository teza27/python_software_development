def factorial():
    print("Welcome to the Teza factorial calculator")
    factorial = 1
    user_input = int(input("Enter the number for which you want to calculate its factorial\n"))

    if user_input == 0:
        print(1)
    else:
        new = user_input + 1
        for num in range(1, new):
            factorial *= num
        print(factorial)
factorial()