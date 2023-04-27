with open("pierwsze.txt") as file:
    primes = [int(x.strip()) for x in file.readlines()]

with open("liczby.txt") as file:
    nums = [int(x.strip()) for x in file.readlines()]

def isPrime(number: int) -> bool:
    if (number == 1) or (number == 0):
        return False
    
    for divisor in range(2, number-1):
        if number % divisor == 0:
            return False

    return True 

def ex_4_1():
    return [x for x in nums if (100 <= x <= 5000) and isPrime(x)]

def ex_4_2():
    return [x for x in primes if isPrime(int(str(x)[::-1]))]

def sumNumberElements(number: int) -> int:
    #rekursywnie liczy sume liczb z ktorych sklada sie liczba
    if len(str(number)) == 1:
        return number

    total = 0
    for digit in str(number):
        total += int(digit)
    return sumNumberElements(total)

def ex_4_3():
    #zwraca dlugosc listy liczb ktore od tylu maja sume == 1
    return len([x for x in primes if sumNumberElements(int(str(x)[::-1])) == 1])

print(ex_4_1())
print(ex_4_2())
print(ex_4_3())