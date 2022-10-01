# Prompt the user for input
purchaseAmount = eval(input("Enter purchase amount: "))

print("purchaseAmount: ", purchaseAmount)
# Compute sales tax
tax = purchaseAmount * 0.10

# Display tax amount with two digits after decimal point
print("Sales tax is", int(tax * 100) / 100.0)
