def calculate(amount, percent):
    return (amount * percent) / 100
def calculate_income_tax(total_income: float) -> float:
    if total_income <= 250000:
        return 0
    elif total_income <= 400000 and total_income > 250000:
        return calculate(total_income - 250000, 15)
    elif total_income <= 800000 and total_income > 400000:
        return calculate(total_income - 400000, 20) + 22500
    elif total_income <= 2000000 and total_income > 800000:
        return calculate(total_income - 800000, 25) + 102500
    elif total_income <= 8000000 and total_income > 2000000:
        return calculate(total_income - 2000000, 30) + 402500
    else:
        return calculate(total_income - 8000000, 35) + 2202500

if __name__ == '__main__':
    annual_income = float(input("Enter annual income:"))

    tax = calculate_income_tax(annual_income)
    print(f"Your annual tax is: {tax}")
    print(f"Your monthly tax is: {tax/12}")
