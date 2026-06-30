
# Declaring variables
investment = 0
rate = 0
years = 0
months = 0
monthly_rate = 0
total = 0

#Request for investment input from client
print("Enter monthly investment amount (Greater than 0 and less than 50000): ")
investment = int(input())

while investment <= 0 or investment >= 50000:
    print("Invalid amount. Must be > 0 and < 50,000.")
    print("Enter monthly investment amount: ")
    investment = int(input())


# Request interest rate of the client
print("Enter yearly interest rate (greater than 0 and less than 15): ")
rate = int(input())

while rate <= 0 or rate >= 15:
    print("Invalid rate. Must be > 0 and < 15.")
    print("Enter yearly interest rate (%): ")
    rate = int(input())


#Request for duration of investment
print("Enter number of years (greater than 0): ")
years = int(input())

while years <= 0:
    print("Invalid duration. Must be greater than 0.")
    print("Enter number of years: ")
    years = int(input())


#Arithemtic behind investement calculation
months = years * 12
monthly_rate = rate / 12 / 100
total = 0
# loop to calculate the investment compounded monthly
for month in range(1, months + 1):

    # Add monthly investment
    total = total + investment

    # Calculate interest
    interest = total * monthly_rate
    interest = round(interest, 2)

    # Add interest to total
    total = total + interest

    # Check if full year
    if month % 12 == 0:
        current_year = month // 12
        print("Year " + str(current_year) + " Total: $" + str(round(total, 2)))


#Final Output
print("/nInvestment Duration:" + str(years) + " years")
print("Yearly interest Rate: " + str(rate) + "%")
print("Monthly Investment: $" + str(investment))
print("Total Amount of Investment After Compounding: $" + str(round(total, 2)))
#print("\nCompleted by, Keith C. Gama")
