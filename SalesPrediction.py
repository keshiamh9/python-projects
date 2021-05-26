#A company has determined that its annual profit is typically 23 percent of total sales. Write
#a program that asks the user to enter the projected amount of total sales, and then displays
#the profit that will be made from that amount.
#Hint: use the value 0.23 to represent 23 percent.

projectedSales = input("Enter the projected amount of total sales: ")
projectedProfit = 0

projectedProfit = float(projectedSales) * .23

print("The profit made from the projected total sales will be: $",projectedProfit)

#I will add onto this program by rounding the output to the nearest 100th decimal

print("The profit rounded to the nearest 100th decimal is: $",(round(projectedProfit, 2)))