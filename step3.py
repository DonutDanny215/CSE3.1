sandwich_type = ""
sandwich_price = ""
subtotal = 0.0
# Explaining Menu options
print("What type of Sandwich would you like?")
print("Chicken $5.25, Beef $6.25, Tofu $5.75")
sandwich_type = ("Sandwich Choice: ")

# Calculating Sandwich Price
if sandwich_type == "Chicken":
    print("You chose Chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "Tofu":
    print("You chose Tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose Beef, which will be $6.25")
    subtotal += 6.25


beverage_size = ""
beverage_price = ""
subtotal = 0.0

print("What size of beverage would you like?")
print("Small $1.00, Medium $1.75, Large $2.25")
beverage_size = ("Beverage Choice: ")

if beverage_size == "Small":
    print("You chose Small, which will be $5.25")
    subtotal += 5.25
elif beverage_size == "Medium":
    print("You chose Tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose Large, which will be $6.25")
    subtotal += 6.25

























