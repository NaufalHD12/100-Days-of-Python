# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to The Tip Calculator!:D")
total_bill = float(input("What was the total bill? $ "))
percen_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_split = int(input("How many people to split the bill? "))

bill_add_tip = (total_bill) + ((total_bill * (percen_tip / 100)))
bill_each_person = bill_add_tip / (people_split)
print("Each person should pay", round(bill_each_person, 2))
