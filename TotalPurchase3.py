def main():
    subtotal = 0

    for counter in range(1, 6):
        itemPrice = float(input('Enter the price of item {}: $'.format(counter)))
        subtotal = subtotal + itemPrice

    print('Your subtotal is: $', (round(subtotal, 2)))
    print('The sales tax is: $', (round((subtotal * .06), 2)))
    print('Your total is: $', (round(subtotal, 2)) + (round((subtotal * .06))))


print("\nYou are purchasing 5 items. Enter the price of each item "
      "to get the subtotal, the sales tax, and the total.")

main()
