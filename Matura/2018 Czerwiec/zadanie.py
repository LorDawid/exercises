with open("dane1.txt") as file:
    data1 = [x.strip().split() for x in file.readlines()]

with open("dane2.txt") as file:
    data2 = [x.strip().split() for x in file.readlines()]

#zmieniamy wszystkie liczby z stringow na integery    
data1 = [[int(x) for x in y] for y in data1]
data2 = [[int(x) for x in y] for y in data2]

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
            if number % 2 == 0:
                even1 += 1
            else:
                odd1 += 1
        
        even2 = 0
        odd2 = 0
        for number in numbers2:
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
    result = []

    for numbers1, numbers2 in zip(data1, data2):

        sorted1 = sorted(numbers1)
        sorted2 = sorted(numbers2)

        data3 = []

        while True:
            if len(sorted1) == 0:
                data3 += sorted2
                break

            if len(sorted2) == 0:
                data3 += sorted1
                break

            val1 = sorted1[0]
            val2 = sorted2[0]

            #c2 jest wiekszy
            if val1 < val2:
                data3.append(val1)
                sorted1.pop(0)

            #c1 jest wiekszy
            if val2 <= val1:
                data3.append(val2)
                sorted2.pop(0)

        result.append(data3)

    return result

def ex_4_4_inaczej():
    #w inny szybszy sposob ale zakladam ze jest niezgodny z poleceniem zadania
    #bo po prostu laczy dwie listy i sortuje wynik

    result = []
    for numbers1, numbers2 in zip(data1, data2):
        combined = numbers1+numbers2
        result.append(sorted(combined))

    return result


print(ex_4_1()) #zadanie 1
print(ex_4_2()) #zadanie 2
print(ex_4_3(), len(ex_4_3())) #UWAGA: pokazuja sie wiersze o 1 mniejsze ze wzgledu na indeksowanie - zeby to zmienic wystarczy zamienic linijke na: print([x+1 for x in ex_4_3()], len(ex_4_3()))
print(ex_4_4()) #zadanie 4
# print(ex_4_4_inaczej()) #zadanie 4 zrobione inaczej, ale zakladam ze jest to nie do konca zgodne z poleceniem bo wykorzystuje inny algorytm

