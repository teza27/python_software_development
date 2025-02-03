
minutesInput = input("How many minutes do you want to convert to hour? ")

minutesInput = int(minutesInput)
hour = minutesInput // 60
minutes = minutesInput % 60
#if hour > 1: print(f"{hour}hours {minutes}minutes")
#else: print(f"{hour}hour {minutes}minutes")

converted = f"{hour}hours {minutes}minutes" if hour > 1 else f"{hour}hour {minutes}minutes"
print(converted)