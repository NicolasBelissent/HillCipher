import numpy as np

B = input("What is the word you want to decode (words) ?")
B = B.lower()
Transform2 = [];
for character in B:
    number = (ord(character) - 97 )%26;
    Transform2.append(number);

def split(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

list(split(Transform2, 2))


N = (list(split(Transform2, 2)))

l = len(N)
for i in l:
    print(N[i])

from N[0] to N[l]


N = (list(split(Transform2, 2)))
#print(N)
key2 = [[15, 17],[20, 9]]
#q = ((np.matmul(key2,N)) % 26)
#print(q)
#first_items = [N for data in N]
#print(first_items)

#for all(list) in N:
 #   X = ((np.matmul(key2,N)) % 26)

#print(X)


#C1 = ((np.matmul(key2, N[0])) % 26)
#D1 = np.array(C1).flatten().tolist()
#C2 = ((np.matmul(key2, N[1])) % 26)
#D2 = np.array(C2).flatten().tolist()

#FinalDecodeNum = D1 + D2
#FinalDecodeChar = []
#for number in FinalDecodeNum:
    #character = (str(chr(number + 97)))
    #FinalDecodeChar.append(character)

#print("This is your coded message:")
#print(FinalDecodeChar)




