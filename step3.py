sandwich_type = ""
sandwich_price = ""

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




