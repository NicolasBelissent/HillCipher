import numpy as np


# alphabet definition (subset of ascii)
alphabetStart = 97
alphabetEnd = 123
alphabetSize = alphabetEnd - alphabetStart

# converts word from letter to number vector
def toNumber(x):
    intArray = []
    for character in x:
        number = (ord(character) - alphabetStart) % alphabetSize
        intArray.append(number)

    return intArray

#converts an integer vector to a word
def toLetter(intArray):
    word = ""
    for number in intArray:
        character = (str(chr(int(number) + alphabetStart)))
        word += character

    return word

# return a list of segment length of 2, or 3
# ex: 4 ==> [2,2]
# ex: 5 ==> [3,2]
# ex: 6 ==> [3,3]
# ex: 7 ==> [3,2,2]
# ex: 8 ==> [3,3,2]
# ex: 9 ==> [3,3,3]
def cut(l):
    segments = []
    z = l % 3
    q = int(np.floor(l / 3))
    if z == 0:
        for i in range(0, q):
            segments.append(3)
    elif z == 1:
        for i in range(0, q-1):
            segments.append(3)
        segments.append(2)
        segments.append(2)
    elif z == 2:
        for i in range(0, q):
            segments.append(3)
        segments.append(2)

    return segments

# takes the submitted word and splits it into pieces corresponding with the results of the cut function.
# ex: "hello" -> toNumber("hello") = [19,5,9,23,14]  ;  cut(len(hello))=[3,2]  ;  split(len(hello))=[19,5,9][23,14]
def split(l):
    list = []
    segmentLengths = cut(len(l))
    offset = 0
    for k in segmentLengths:
        segment = []
        for i in range(0, k):
            segment.append(l[offset])
            offset = offset + 1
        list.append(segment)

    return list

class HillCipher:
    key2 = [[3, 3], [2, 5]]
    invKey2 = [[15, 17],[20, 9]]
    key3 = [[6,24,1],[13,16,10],[20,17,15]]
    invKey3 = [[8,5,10],[21,8,21],[21,12,8]]

    def __init__(self):
        pass

    def encode(self, word):
        word = word.lower()
        a = toNumber(word)
        b = split(a)
        out = []
        for j in b:
            if len(j) == 2:
                x = (np.matmul(self.key2, j)) % alphabetSize
                y = np.array(x).flatten().tolist()

            elif len(j) == 3:
                x = (np.matmul(self.key3, j)) % alphabetSize
                y = np.array(x).flatten().tolist()

            print(y)
            out += y

        return toLetter(out)

    def decode(self, word):
        word = word.lower()
        a = toNumber(word)
        b = split(a)
        out = []
        for j in b:
            if len(j) == 2:
                x = (np.matmul(self.invKey2, j)) % alphabetSize
                y = np.array(x).flatten().tolist()

            elif len(j) == 3:
                x = (np.matmul(self.invKey3, j)) % alphabetSize
                y = np.array(x).flatten().tolist()

            print(y)
            out += y

        return toLetter(out)

    def isValidCharacter(self, character):
        return ord(character) >= alphabetStart and ord(character) < alphabetEnd
