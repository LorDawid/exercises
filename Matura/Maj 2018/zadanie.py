with open("sygnaly.txt") as file:
    words = [x.strip() for x in file.readlines()]

def ex_4_1():
    finalWord = ""

    for wordIndex in range(39, len(words), 40):
        finalWord += words[wordIndex][9]

    return finalWord

def ex_4_2():
    uniqueLetters = {}
    for word in words:
        letters = set()
        for letter in word:
            letters.add(letter)
        uniqueLetters[word] = len(letters)

    sortedLetters = sorted(uniqueLetters.items(), key = lambda item: item[1])

    return sortedLetters[-1]

def ex_4_3():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    distances = []
    for word in words:
        maxDistance = -1
        for letter1 in word:
            for letter2 in word:
                maxDistance = max(maxDistance, abs(letters.find(letter1) - letters.find(letter2)))

        distances.append([word, maxDistance])
    
    validWords = []

    for word, maxDistance in distances:
        if maxDistance <= 10:
            validWords.append(word)

    return validWords

print(ex_4_1()) #zadanie 1
print(ex_4_2()) #zadanie 2
print(ex_4_3()) #zadanie 3