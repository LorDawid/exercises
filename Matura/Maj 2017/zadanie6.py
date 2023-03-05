imageData = []

with open("dane.txt") as file:
    for info in file.readlines():
        imageData.append([int(x) for x in info.strip().split()])

def ex6_1():
    darkest, lightest = 0, 0
    for line in imageData:
        for value in line:
            if value < darkest: darkest = value
            if value > lightest: lightest = value

    return lightest, darkest

# print(f"Najjasniejszy i najciemniejszy piksel: {ex6_1()}")

def isSymmetrical(linia: list[int]) -> bool:
    return linia[::-1] == linia

def ex6_2():
    niesymetryczne_linie = 0
    for line in imageData:
        if not isSymmetrical(line):
            niesymetryczne_linie += 1

    return niesymetryczne_linie

# print(f"Aby obraz byl symetryczny trzeba usunac {ex6_2()} linijek")

