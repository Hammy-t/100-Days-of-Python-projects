#Code to calculate the total amount each person is to pay 
#depending on the specified percentage of tip

def calc(total, tip, noOfPeople):
    tipAmount = total*(tip/100)
    amountToPay = (tipAmount+ total)/noOfPeople
    return round(amountToPay,2), round(tipAmount,2)

def main():
    print("Welcome to the tip calculator")
    total = float(input("What was the total bill? "))
    tip = float(input("What percentage of tip would you like to give? "))
    noOfPeople = float(input("How many people are splitting the bill? "))
    return (calc(total, tip, noOfPeople))

amountToPay,tipAmount = main()
print("Amount per person is $" + str(amountToPay))
print("Total tip is $" + str(tipAmount))