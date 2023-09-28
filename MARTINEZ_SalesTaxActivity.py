#prompts the user to enter his details
Name = input("Please enter your name       : ")
pA = float(input("Enter your purchase amount   : "))

#formula for the added sales tax
salesTax = pA * 0.06
totalAmount = salesTax + pA

#display
print()
print(f"{Name}'s total amount to be paid: {totalAmount:.2f}")
print(f"Your purchase amount         : {pA:.2f}")
print(f"Added Sales tax              : {salesTax:.2f}")
