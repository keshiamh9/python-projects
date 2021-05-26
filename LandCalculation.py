#One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
#enter the total square feet in a tract of land and calculates the number of acres in the tract.
#Hint: divide the amount entered by 43,560 to get the number of acres

totalSqFt = input("This program calculates the number of acres in a tract of land.\nEnter the total square feet in a tract of land: ")
totalAcres = float(totalSqFt) / 43560

print("The number of acres in the tract of land entered is: ", (round(totalAcres, 2)), "acres")
