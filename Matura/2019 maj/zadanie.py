import math

with open("przyklad.txt") as file:
    data = [int(x.strip()) for x in file.readlines()]

def ex_4_1():
    result = 0

    for number in data:
        power = math.log(number, 3)
        if power % 1 == 0: result += 1

    return result

def ex_4_2():
    result = 0

    for number in data:
        factorialSum = 0

        #korzystajac z wbudowanej biblioteki math
        for digit in str(number):
            factorialSum += math.factorial(int(digit))

        #korzystajac ze zwyklego algorytmu
        # for digit in str(number):
            # digit = int(digit)
            
            # factorial = 1
            # for i in range(digit, 0, -1):
                # factorial *= i

            # factorialSum += 1

        if factorialSum == number: result += 1

    return result
        

print(ex_4_1()) #zadanie1
print(ex_4_2()) #zadanie2