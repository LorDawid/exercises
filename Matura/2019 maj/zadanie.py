import math

with open("liczby.txt") as file:
    data = [int(x.strip()) for x in file.readlines()]

def ex_4_1():
    result = 0

    for number in data:
        power = math.log(number, 3)
        if power % 1 == 0: result += 1

    return result

def ex_4_2():
    results = []

    for number in data:
        factorialSum = 0

        #korzystajac z wbudowanej biblioteki math
        # for digit in str(number):
            # factorialSum += math.factorial(int(digit))

        #korzystajac ze zwyklego algorytmu
        for digit in str(number):
            digit = int(digit)
            
            factorial = 1
            for i in range(1, digit + 1):
                factorial *= i

            factorialSum += factorial

        if factorialSum == number: results.append(number)

    return results

def dzielniki(number: int) -> list[int]:
    result = []

    for divisor in range(number, 0, -1):
        if number % divisor == 0: result.append(divisor)

    return result

def nwd(num1: int, num2: int) -> int:
    divs1 = dzielniki(num1)
    divs2 = dzielniki(num2)
    common = []

    for number in divs1:
        if number in divs2: common.append(number)

    return max(common)

class Dzielniki:
    def __init__(self, startnum: int) -> None:
        self.numbers = [startnum]
        self.nwd = startnum

    #zwraca true/false w zalenosci od tego czy liczba ma wspolne dzielniki
    def addNumber(self, number: int) -> bool:
        divisor = nwd(self.nwd, number)

        if divisor > 1:
            self.nwd = divisor
        else:
            return False

        self.numbers.append(number)
        return True

    def __str__(self) -> str:
        return f"Pierwsza liczba: {self.numbers[0]}, dlugosc: {len(self.numbers)}, nwd: {self.nwd}"

def ex_4_3():
    #JESZCZE NIE DZIALA

    nums = []

    temp = Dzielniki(data[0])
    for number in range(len(data)):
        if not temp.addNumber(data[number]):
            nums.append(temp)
            temp = Dzielniki(data[number+1])

    longestList = -1
    longestVal = None
    for number in nums:
        if len(number.numbers) > longestList:
            longestList = len(number.numbers)
            longestVal = number

    return longestVal

print(ex_4_1()) #zadanie1
print(ex_4_2()) #zadanie2
print(ex_4_3()) #zadanie3
