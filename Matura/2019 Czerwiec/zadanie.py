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
    #zwraca dlugosc listy liczb ktore od tylu maja sume = 1
    return len([x for x in primes if sumNumberElements(x) == 1]) # Nie ma sensu liczyć dla liczb, które czytamy od tyłu. Wynik jest ten sam, ale w innym zadaniu taki błąd mógłby wpłynąc na poprawność odpowiedzi

ex1 = ",\n".join(str(x) for x in ex_4_1()) #zadanie 1
ex2 = ",\n".join(str(x) for x in ex_4_2()) #zadanie 2
ex3 = ex_4_3() #zadanie 3
#czas wykonanie: 20 minut

with open("wyniki1.txt", "w") as file:
    file.write(f"""
Zad1:
{ex1}

Zad2:
{ex2}

Zad3:
{ex3}
""")