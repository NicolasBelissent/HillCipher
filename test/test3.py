from src.HillCipher import HillCipher

x = input('What do you want to encode ? ');


cipher = HillCipher()
encoded = cipher.encode(x)
print("Encoded word : ", encoded)
print("Decoded word :", cipher.decode(encoded))
