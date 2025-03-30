
import random , string


# here we will learn to encryptand decrypt text 

chars = " "+ string.ascii_letters + string.punctuation + string.digits

chars = list(chars) # convert chars into list

key = chars.copy()  # make a copy of origional to shuffle

random.shuffle(key)
cipher_text = " "
# for encryption
plain_text = input("Enter your text to encrypt : ")

for letter in plain_text:
    index = chars.index(letter)
    cipher_text +=key[index]

print(cipher_text)


# for decryption

cipher_text = input("Enter your text to encrypt : ")
plain_text_text = " "
for letter in cipher_text:
    index = key.index(letter)
    plain_text_text +=chars[index]
    
print(cipher_text)
print(plain_text_text)




