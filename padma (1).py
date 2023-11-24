import cv2
import os
import string
import sys

dictionary = {}
char = {}
# Converting and saving characters ASCII numbers
for i in range(255):
    dictionary[chr(i)] = i
    char[i] = chr(i)


# Encrypting function
def Encrypt():
    key_length = 0
    length = len(message)
    n = 0
    m = 0
    z = 0
    # for loop for XOR of message
    # With password with rgb pixels of image
    # (stenography in lsb of rgb)

    for i in range(length):
        image[n, m, z] = dictionary[message[i]] ^ dictionary[password[key_length]]
        n = n + 1
        m = m + 1
        m = (m + 1) % 3
        key_length = (key_length + 1) % len(password)

    cv2.imwrite("Encrypted_image.jpg", image)  # saving/writing the encrypted image
    os.startfile("Encrypted_image.jpg")
    print("Encryption Done\n")
    print("Thank You!")


# Decryption function
def Decrypt(encrypted_image, password, length):
    key_length = 0
    n = 0
    m = 0
    z = 0
    decode = ""
    # Re xor ing for decryption
    for i in range(length):
        decode += char[image[n, m, z] ^ dictionary[password[key_length]]]
        n = n + 1
        m = m + 1
        m = (m + 1) % 3
        key_length = (key_length + 1) % len(password)

    print("Decrypted text:", decode)
    print("Thank You!")


# Menu bar
while True:
    print("------------------Menu--------------------\n")
    print("Enter\n1 to Encrypt message\n2 to Decrypt message\n3 to Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        image = cv2.imread("new.jpg")  # Allocating path of image
        pointer1 = image.shape[0]  # use new.jpg as an image to encrypt
        pointer2 = image.shape[1]  # or change your input image name to "new" and int's format should be in jpg itself
        password = input("Enter the Password to encrypt: ")
        message = input("Enter the message: ")
        Encrypt()
    elif choice == 2:
        image_path = "Encrypted_new.jpg"  # Allocating path of encrypted image
        encrypted_image = cv2.imread(image_path)
        password = input("Enter the password to decrypt: ")
        length = len(message)
        Decrypt(encrypted_image, password, length)
    elif choice == 3:
        sys.exit(0)