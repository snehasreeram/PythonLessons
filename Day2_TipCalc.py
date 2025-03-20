#Create a Tip Calculator#

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?: $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15?: "))
people = int(input("How many people to split the bill?: "))

share = round((bill + (bill*(tip_percent/100)))/people,2)

print (f"Each person should pay: ${share}")
