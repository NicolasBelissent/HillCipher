import numpy as np
# from convertutil import split, toNumber, toLetter

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

