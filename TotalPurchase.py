# A customer in a store is purchasing five items.
# Write a program that asks for the price of
# each item, and then displays the subtotal of
# the sale, the amount of sales tax, and the total.
# Assume the sales tax is 6 percent.

print("You are purchasing 5 items. Enter the price of each item"
      "to get the subtotal, the sales tax, and the total.")
item1 = input("Item 1 price: ")
item2 = input("Item 2 price: ")
item3 = input("Item 3 price: ")
item4 = input("Item 4 price: ")
item5 = input("Item 5 price: ")

subTotal = float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
totalSalesTax = subTotal * .06
total = subTotal + totalSalesTax

print("Your subtotal is: $", (round(subTotal, 2)), "\nThe sales tax is: $", (round(totalSalesTax, 2)),
      "\nYour total is: $", (round(total, 2)))
