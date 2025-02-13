from functools import reduce
sample_data = [200, 455.23, -306.5, 25000, -642.21, -133.9, 79.79, 1300, 5000, 3400, -150, -790, -3210, -1000, 8500, -30]

savings = sum(filter(lambda x : x != 0, list(map(lambda x : round(x * 0.05 if x > 0 else 0, 2), sample_data))))
print(f"Your total savings for the period is ${savings}")

total_amount = reduce(lambda x, y : x + y, sample_data)
print(f"Total money you have received is ${total_amount}")