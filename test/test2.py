import numpy as np

A = input('What do you want to encode (4 words)');
A = A.lower()

print(A)
class Convert:
    def __init__(self,x):

        def ToNumber(self,x):
            Transform1 = []
            for character in x:
                number = (ord(character) - 97) % 26
                Transform1.append(number)

        def ToLetter(self,x):
            Transform2 = []
            for number in x:
                character = (str(chr(number + 97)))
                Transform2.append(character)

        def split(l, n):
        # For item i in a range that is a length of l,
            for i in range(0, len(l), n):
            # Create an index range for l of n items:
                yield l[i:i + n]

Z = Convert()
Z.ToNumber(A)

A1 = ToNumber()

A2 = list(split(Transform1, A1))

key = [[3, 3], [2, 5]]
X1 = ((np.matmul(key, M[0])) % 26)
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

