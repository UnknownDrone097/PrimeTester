def IsPrime(number):
    divisor = 2

    while (number % divisor) != 0 and divisor <= int(number ** .5):
        if (divisor == 2):
            divisor += 1
            continue
        else:
            divisor += 2
    else:
        if (number % divisor) == 0:
            return(number, divisor, 'Not prime')
        else:
            return(number, 'Prime')

print(IsPrime(float(input('Number?\n'))))
