def compound_interest(principal, annual_rate, times_compounded, years):
    # Calculate the compound interest
    amount = principal * (1 + annual_rate / times_compounded) ** (times_compounded * years)
    # Calculate the interest earned
    interest = amount - principal
    return interest

# Example usage:
principal_amount = 1000  # the initial amount of money
annual_interest_rate = 0.05  # annual interest rate (5%)
compounding_frequency = 4  # quarterly compounding
investment_duration = 5  # number of years

interest_earned = compound_interest(principal_amount, annual_interest_rate, compounding_frequency, investment_duration)
print("Interest earned:", round(interest_earned, 2))
