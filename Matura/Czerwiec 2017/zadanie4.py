points = []

with open("punkty.txt") as file:
    for point in file.readlines():
        pointValue = point.strip().split()
        pointValue = tuple(int(x) for x in pointValue)
        points.append(pointValue)

def isPrime(num: int) -> bool:
    if num < 2: return False
    for divider in range(2, num-1):
        if num % divider == 0: return False
    return True

def ex4_1() -> int:
    primes = 0
    for point in points:
        primes += isPrime(point[0]) and isPrime(point[1])

    return primes

def ex4_2() -> int:
    sameNumbers = 0
    for point in points:
        if set(str(point[0])) == set(str(point[1])): sameNumbers += 1

    return sameNumbers

from math import sqrt
def getDistance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    return sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def ex4_3() -> tuple[tuple[int, int], tuple[int, int]]:
    biggest = 0.0
    pair = tuple()
    for pointA in points:
        for pointB in points:
            distance = getDistance(pointA, pointB)
            if distance > biggest:
                biggest = distance
                pair = (pointA, pointB)

    return pair

def ex4_4() -> tuple[int, int, int]:
    inside = 0
    onside = 0
    outside = 0
    for point in points:
        if     ((point[0] <  5000) and (point[1] <  5000)): inside += 1
        if not ((point[0] <= 5000) and (point[1] <= 5000)): outside += 1

        if ((point[0] == 5000) and (point[1] < 5000) or
            (point[1] == 5000) and (point[0] < 5000)):
                onside += 1


    return inside, onside, outside

# print(f"Zadanie 1: {ex4_1()}")
# print(f"Zadanie 2: {ex4_2()}")
# print(f"Zadanie 3: {ex4_3()}")
# print(f"Zadanie 4: {ex4_4()}")

#Czas wykonania zadania: 20min 16s
#bezblednie za pierwszym razem z czego jestem bardzo dumny