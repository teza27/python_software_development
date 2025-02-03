"""This code takes user's transaction data as input, notifies the customer on debit/credit and calculates the balance
sample_data = 200, 455.23, -306.5, 25000, -642.21, -133.9, 79.79, 1300, 5000, 3400, -150, -790, -3210, -1000, 8500, -30
"""
balance = 0
tran_entry = input("List the amounts that have been debited and credited to your account this month. Seperate each by comma and space\n")
tran_split = tran_entry.split(", ")
tran_list = []
for amount in tran_split:
    if "." in amount:
        tran_digit = float(amount)
    else:
        tran_digit = int(amount)
    tran_append = tran_list.append(tran_digit)
for tran in tran_list:
    balance = round(balance + tran, 2)
    if tran > 0:
        print(f"Your account has been credited with ${tran} and your balance is ${balance}")
    else:
        print(f"Your account has been debited with ${tran} and your balance is ${balance}")
print(f"Your available balance is ${balance}")