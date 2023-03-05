imageData = []

with open("dane.txt") as file:
    for info in file.readlines():
        imageData.append([int(x) for x in info.strip().split()])

def ex6_1() -> tuple[int, int]:
    #Podaj jasność najjaśniejszego i jasność najciemniejszego piksela. 
    darkest, lightest = 0, 0
    for line in imageData:
        for value in line:
            if value < darkest: darkest = value
            if value > lightest: lightest = value

    return lightest, darkest


def isSymmetrical(linia: list[int]) -> bool:
    return linia[::-1] == linia

def ex6_2() -> int:
    #Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetrii.
    nonSymmetrical = 0
    for line in imageData:
        if not isSymmetrical(line):
            nonSymmetrical += 1

    return nonSymmetrical


def getNeighbours(x: int, y: int) -> bool:
    #jestem bardzo dumny z tego rozwiazania, jest calkiem szybkie
    #przechodzimy przez kazdy piksel i bierzemy wartosci pikseli
    #po jego lewej prawej gorze i dole, clampujemy te wartosci do
    #maksymalnych wartosci obrazu, zeby nie bylo IndexErroru na kazdym
    #brzegowym pikselu, jesli roznica miedzy ktoryms z pikseli
    #jest wieksza niz 128, zwracamy prawde.

    currentPixel = imageData[y][x]
    neighbours = [
        imageData[y][min(x+1, 319)],
        imageData[y][max(x-1, 0  )],
        imageData[max(y-1, 0  )][x],
        imageData[min(y+1, 199)][x],
    ]

    for neighbour in neighbours:
        if abs(neighbour - currentPixel) > 128:
            return True

    return False

def ex6_3() -> int:
    #Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel. 
    contrasting = 0
    for y, line in enumerate(imageData):
        for x in range(len(line)):
            contrasting += getNeighbours(x, y)

    return contrasting


def ex6_4():
    #Podaj długość najdłuższej linii pionowej złożonej z pikseli tej samej jasności.
    consecutive = -1

    for x in range(320):
        currentConsecutives = 0
        lastvalue = -1
        for y in range(200):
            value = imageData[y][x]
            if value == lastvalue:
                currentConsecutives += 1
            else:
                consecutive = max(currentConsecutives, consecutive)
                currentConsecutives = 1

            lastvalue = value

    return consecutive

# print(f"Najjasniejszy i najciemniejszy piksel: {ex6_1()}")
# print(f"Aby obraz byl symetryczny trzeba usunac {ex6_2()} linijek")
# print(f"Liczba kontrastujacych pikseli: {ex6_3()}")
# print(f"Najdluzsza linia pionowa: {ex6_4()}")