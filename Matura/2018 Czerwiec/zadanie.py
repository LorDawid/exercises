with open("przyklad1.txt") as file:
    data1 = [x.strip().split() for x in file.readlines()]

with open("przyklad2.txt") as file:
    data2 = [x.strip().split() for x in file.readlines()]

def ex_4_1():
    sameEndings = 0
    for numbers1, numbers2 in zip(data1, data2):
        if numbers1[-1] == numbers2[-1]:
            sameEndings += 1

    return sameEndings

def ex_4_2():
    validNumbers = 0
    for numbers1, numbers2 in zip(data1, data2):

        even1 = 0
        odd1 = 0
        for number in numbers1:
            number = int(number)
            if number % 2 == 0:
                even1 += 1
            else:
                odd1 += 1
        
        even2 = 0
        odd2 = 0
        for number in numbers2:
            number = int(number)
            if number % 2 == 0:
                even2 += 1
            else:
                odd2 += 1

        if even1 == odd1 == even2 == odd2 == 5: validNumbers += 1

    return validNumbers

def ex_4_3():
    results = []

    for index, numbers in enumerate(zip(data1, data2)):
        digits1 = set(x for x in numbers[0])
        digits2 = set(x for x in numbers[1])
        
        if digits1 == digits2:
            results.append(index)

    return results

def ex_4_4():
    print("NIESKONCZONE JESZCZE")

    allNumbers = []

    for numbers1, numbers2 in zip(data1, data2):
        numbers3 = []

        for digit1, digit2 in zip(numbers1, numbers2):
            numbers3.append(min(digit1, digit2))

        allNumbers.append(numbers3)

    return allNumbers


print(ex_4_1()) #zadanie 1
print(ex_4_2()) #zadanie 2
print(ex_4_3(), len(ex_4_3())) #zadanie 3 - pokazuja sie wiersze 0,4 ze wzgledu na indeksowanie pythona ale w praktyce sa to 1,5
# print(ex_4_4()) #zadanie 4
