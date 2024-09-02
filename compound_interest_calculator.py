principle = 0
rate = 0
time = 0

while (principle <= 0):
    principle = float(input("Enter the Principle: "))

    if (principle <= 0):
        print("Principle cannot be less than or equal to 0")

while (rate <= 0):
    rate = float(input("Enter the Rate: "))

    if (rate <= 0):
        print("Rate cannot be less than or equal to 0")


while (time <= 0):
    time = int(input("Enter the Time (years): "))

    if (time <= 0):
        print("Time cannot be less than or equal to 0")


total = principle * pow((1 + rate/100),time)
print(f"Balance after {time} years is {total:.2f}")