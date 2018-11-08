curBalance = float(input("Enter current bank balance:"))
interestRate = float(input("Enter interest rate:"))
time = int(input("Enter the amount of time that passes:"))

def calcMoney(value, interest, time):
	return value * (1 + interest) ** time

print(calcMoney(curBalance, interestRate, time))