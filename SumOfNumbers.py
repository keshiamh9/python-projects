# Write a program with a loop that asks the user to enter a series of positive numbers. The
# user should enter a negative number to signal the end of the series. After all the positive
# numbers have been entered, the program should display their sum.

def main():
    total = 0
    number = int(input('\nEnter a positive number. Enter a negative number to end program: '))
    while number > 0:
        total = total + number
        number = int(input('Enter a positive number. Enter a negative number to end program: '))
    if number < 0:
        print('The total of the positive numbers is: ', total)


main()
