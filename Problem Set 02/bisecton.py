balance = 999999
annualInterestRate = 0.18


def balance_left_after_a_year(balance, annual_interest_rate, monthly_pay):
    for i in range(1, 13):
        balance -= monthly_pay
        balance += annual_interest_rate * balance / 12.0
    return balance

lower_bound = balance / 12.0
upper_bound = (balance * (1 + (annualInterestRate/12.0))**12) / 12.0

while(True):
    monthly_pay = (lower_bound + upper_bound) / 2
    balance_left = balance_left_after_a_year(balance,
                                             annualInterestRate,
                                             monthly_pay)
    if balance_left <= 0 and balance_left > -0.01:
        break
    elif balance_left > 0:
        lower_bound = monthly_pay
    else:
        upper_bound = monthly_pay

print "Lowest Payment:", round(monthly_pay, 2)
