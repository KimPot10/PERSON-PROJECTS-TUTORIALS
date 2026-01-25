# Python Compound Interest Calculator

principle = 0
rate = 0 
time = 0

# formula: Final Ammount = principle(1 + rate/input)tsquared

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be zero or less than zero")

while rate <= 0:
    rate = float(input("Enter Interest Rate%: "))
    if rate <= 0:
        print("Interest Rate is not Valid.")
    else:
        rate /= 100 

while time <= 0:
    time = int(input("Enter Time in Years: "))
    if time <= 0:
        print("Time is counted in years")

final = principle*(1 + rate)**time

print("Principle: ", principle)
print("Rate: ", rate)
print("Time in years: ", time)
print("Interest: ", final)