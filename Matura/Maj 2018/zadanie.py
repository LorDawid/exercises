with open("sygnaly.txt") as file:
    words = [x.strip() for x in file.readlines()]

def ex_4_1():
    finalWord = ""

    for wordIndex in range(39, len(words), 40):
        finalWord += words[wordIndex][9]

    return finalWord

def ex_4_2():
    longestWord = ("", -1)
    for word in words:
        uniqueLetters = len(set(word))
        if uniqueLetters > longestWord[1]:
            longestWord = (word, uniqueLetters)

    return longestWord

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

ex1 = ex_4_1() #zadanie 1
ex2 = "\n".join(str(x) for x in ex_4_2()) #zadanie 2
ex3 = "\n".join(ex_4_3()) #zadanie 3

with open("wyniki41.txt", "w") as file:
    file.write(f"""
Zad1:
{ex1}

Zad2:
{ex2}

Zad3:
{ex3}
""")