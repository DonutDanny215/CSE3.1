sandwich = input("What choice of sandwich would you like: Chicken ($5.25), Beef ($6.25), Tofu ($5.75)")
drink = input("Would you like a drink?")
drink_size = "No"
fries = input("Do you want french fries as well?")
fries_size = "None"
ketchup = float(input("How many ketchup packets do you want? ($0.25 per packet)"))
total_cost = 0

if sandwich == "Chicken":
  total_cost = total_cost + 5.25
elif sandwich == "Beef":
  total_cost = total_cost + 6.25
elif sandwich == "Tofu":
  total_cost = total_cost + 5.75

if drink == "Yes":
  drink_size = input("What size drink would you like: Small ($1.00), Medium ($1.75), Large ($2.25)")
  if drink_size == "Small":
    total_cost = total_cost + 1.00
  elif drink_size == "Medium":
    total_cost = total_cost + 1.75
  elif drink_size == "Large":
    total_cost = total_cost + 2.25
else:
  drink = "No Beverage"

if fries == "Yes":
  fries_size = input("What size fries would you like: Small ($1.00), Medium ($1.50), Large ($2.00)")
  if fries_size == "Small":
    super_size = input("Would you like to super-size your fries?")
    if super_size == "Yes":
      fries_size = "Large"
      total_cost = total_cost + 2.00
    else:
      total_cost = total_cost + 1.00
  elif fries_size == "Medium":
    total_cost = total_cost + 1.50
  elif fries_size == "Large":
    total_cost = total_cost + 2.00

ketchup_price = ketchup * 0.25
total_cost = total_cost + ketchup_price

if drink == "Yes":
  if fries == "Yes":
    total_cost = total_cost - 1.00

print(sandwich+" Sandwich")
print(drink_size + " Drink")
print(fries_size + " Fries")
print("$" + str(total_cost))