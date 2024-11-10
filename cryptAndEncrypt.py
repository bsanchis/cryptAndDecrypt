import string
import random

def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))


def encrypt_block(plain_text, key, block_size=4):
    cipher_text = []
    padded_text = plain_text + 'X' * (block_size - len(plain_text) % block_size)
    
    for i in range(0, len(padded_text), block_size):
        block = padded_text[i:i + block_size]
        encrypted_block = ''.join([key[char] for char in block])
        cipher_text.append(encrypted_block)
    
    return ''.join(cipher_text)

def decrypt_block(cipher_text, key, block_size=4):
    reverse_key = {v: k for k, v in key.items()}
    plain_text = []
    
    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i:i + block_size]
        decrypted_block = ''.join([reverse_key[char] for char in block])
        plain_text.append(decrypted_block)
    
    return ''.join(plain_text).rstrip('X')  


key = generate_key()

print("Clé de substitution générée:")
print(key)

message = input("\nEntrez le message à chiffrer (en majuscules, sans espaces): ").upper()

cipher_text = encrypt_block(message, key)
print(f"\nMessage chiffré: {cipher_text}")

decrypted_message = decrypt_block(cipher_text, key)
print(f"\nMessage déchiffré: {decrypted_message}")
print("\n")

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [79, 90, 37, 36, 79, 65, 67, 55, 79, 57, 47, 34,  3, 63, 69, 84, 73,
       81, 80, 10, 48, 14, 71, 22,  4, 59, 96, 81, 66, 76, 23, 40, 67,  7,
       25, 41, 74, 93, 73, 51]
bubbleSort(arr)
print("tableau triée : ",arr)
print("\n")
