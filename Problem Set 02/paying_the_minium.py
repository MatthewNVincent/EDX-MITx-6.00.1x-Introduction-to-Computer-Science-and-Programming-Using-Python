balance = 3926
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
min_monthly_pay = 0
total_paid = 0

for i in range(1, 13):
    print "Month:", i
    min_monthly_pay = monthlyPaymentRate * balance
    total_paid += min_monthly_pay
    balance -= min_monthly_pay
    balance += annualInterestRate * balance / 12.0
    print "Minimum monthly payment:", round(min_monthly_pay, 2)
    print "Remaining balance:", round(balance, 2)

print "Total paid:", round(total_paid, 2)
print "Remaining balance:", round(balance, 2)
