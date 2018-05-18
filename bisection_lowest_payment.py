tests = [
    {
        'balance': 320000,
        'annualInterestRate': 0.2,
        'answer': 29157.09
    },    {
        'balance': 999999,
        'annualInterestRate': 0.18,
        'answer': 90325.02
    },    {
        'balance': 53425,
        'annualInterestRate': 0.21,
        'answer': 4889.04
    },    {
        'balance': 471238,
        'annualInterestRate': 0.18,
        'answer': 42564.62
    }
]

balance = tests[2]['balance']
annualInterestRate = tests[2]['annualInterestRate']

low = balance / 12.0  # monthly payments of 1/12 the original balance
high = (balance*(1+(annualInterestRate/12.0))**12/12.0)  # monthly payments towards 1/12
answer = (low + high) / 2 # mean of low & high

def cycle( pay , bal ): # calculates one year
    for _ in range(1,13):
        bal -= pay
        bal += ((annualInterestRate/12.00) * bal)
    return bal

while True:
    print(low, high) # print low and high limits for each scope
    hold = cycle(answer, balance) # calculate resultant balance
    if abs( hold ) < 0.1: # if the end balance is under threshold, break and print
        print( 'Lowest Payment: ' + str( round(answer, 2) ) )
        break # break out after printing answer
    elif hold < 0:
        # if result if too high, set upper limit as current guess
        high = answer
        answer = (low + high) / 2
    else:
        # if result is too low, set lower limit as current guess
        low = answer
        answer = (low + high) / 2

