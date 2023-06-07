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
        digits1 = set(numbers[0])
        digits2 = set(numbers[1])
        
        if digits1 == digits2:
            results.append(index + 1)

    return results

def ex_4_4():
    result = []

    for numbers1, numbers2 in zip(data1, data2):
        data3 = []

        while True:
            if len(numbers1) == 0:
                data3 += numbers2
                break

            if len(numbers2) == 0:
                data3 += numbers1
                break

            val1 = numbers1[0]
            val2 = numbers2[0]

            #c2 jest wiekszy
            if val1 < val2:
                data3.append(val1)
                numbers1.pop(0)

            #c1 jest wiekszy
            if val2 <= val1:
                data3.append(val2)
                numbers2.pop(0)

        result.append(data3)

    return result

ex1 = ex_4_1()
ex2 = ex_4_2()
ex3 = ex_4_3()
ex4 = "\n".join(", ".join(str(y) for y in x) for x in ex_4_4())

with open("wyniki1.txt", "w") as file:
    file.write(
f"""
Zad1:
{ex1}

Zad2:
{ex2}

Zad3:
{ex3[0]}
{len(ex3)}

Zad4:
{ex4}
""")