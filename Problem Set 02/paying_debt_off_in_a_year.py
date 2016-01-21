balance = 3926
annualInterestRate = 0.2


def will_pay_in_a_year(balance, annual_interest_rate, monthly_pay):
    for i in range(1, 13):
        balance -= monthly_pay
        balance += annual_interest_rate * balance / 12.0
    if balance <= 0:
        return True
    else:
        return False

monthly_pay = 10
while(not will_pay_in_a_year(balance, annualInterestRate, monthly_pay)):
    monthly_pay += 10

print "Lowest Payment:", monthly_pay
