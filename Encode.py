import numpy as np

A = input('What do you want to encode (4 words)');
A = A.lower()
Transform1 = []
for character in A:
    number = (ord(character) - 97) % 26
    Transform1.append(number)


def split(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i + n]
list(split(Transform1, 2))

M = (list(split(Transform1, 2)))
print(M)

key = [[3, 3], [2, 5]]

X1 = ((np.matmul(key, M[0])) % 26)
print(X1)
Y1 = np.array(X1).flatten().tolist()
X2 = ((np.matmul(key, M[1])) % 26)
Y2 = np.array(X2).flatten().tolist()

FinalNumbCode = Y1 + Y2
FinalCharCode = []
for number in FinalNumbCode:
    character = (str(chr(number + 97)))
    FinalCharCode.append(character)

print("This is your coded message:")
print(FinalCharCode)