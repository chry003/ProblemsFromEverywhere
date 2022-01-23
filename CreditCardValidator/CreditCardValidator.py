def ccv(creditCardNumber):
    total = 0
    second = False

    while creditCardNumber != 0:
        lastDigit = creditCardNumber % 10 # Get the last number from the credit card number

        if second:
            doubleOfLastDigit = lastDigit * 2
            
            while doubleOfLastDigit != 0:
                total = total + (doubleOfLastDigit % 10)
                doubleOfLastDigit //= 10

        else: total += lastDigit
        second = not second # change second to false if true or other way around

        creditCardNumber //= 10

    return (total % 10 == 0)

result = ccv(int(input()))

if result: print("It is valid card")
else: print("Invalid Card")
