# Currency Conversion Functions

# Write functions to convert an amount from one currency to another.

### Requirements
# * Define a function `convert_to_usd(krw)`.
# * Define a function `convert_to_krw(usd)`.
# * The functions should return values rounded to two decimal places.
# * Assume the exchange rate is 1 USD = 1300 KRW.
# * Ensure that the functions produce the expected output for the given test cases.

# Define a function to convert KRW to USD
def convert_to_usd(krw):
    # Write your implementation here
    return round(krw/1300, 2)


# Define a function to convert USD to KRW
def convert_to_krw(usd):
    # Write your implementation here
    return round(usd * 1300, 2)

    
