import math

def income_after_years(p, r, t):
    return p * math.exp(r * t)

def years_to_reach_income(p, a, r):
    return math.log(a / p) / r

initial = 10000
rate = 0.05
years = 10

final_income = income_after_years(initial, rate, years)
print(round(final_income, 2))

target = 20000
needed_years = years_to_reach_income(initial, target, rate)
print(round(needed_years, 2))
