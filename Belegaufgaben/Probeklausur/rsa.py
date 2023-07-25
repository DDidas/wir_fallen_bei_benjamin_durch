import string
import sympy
from sympy import mod_inverse

def calculate_d(e, N):
    factors = sympy.factorint(N)
    p, q = list(factors.keys())
    phi = (p-1) * (q-1)
    d = mod_inverse(e, phi)
    return d

def text_to_numbers(text):
    text = text.upper()
    if len(text) % 2 != 0:
        text += ' '
    return ['{:02d}{:02d}'.format(string.ascii_uppercase.index(text[i])+1,
                                  string.ascii_uppercase.index(text[i+1])+1) for i in range(0, len(text), 2)]

def numbers_to_text(numbers):
    nums = [int(str(num)[i:i+2]) for num in numbers for i in range(0, len(str(num)), 2)]
    text = ''.join([string.ascii_uppercase[n-1] if 0 < n <= 26 else ' ' for n in nums])
    return text

def encrypt_rsa(e, N, text):
    numbers = text_to_numbers(text)
    return [pow(int(num), e, N) for num in numbers]

def decrypt_rsa(d, N, encrypted):
    decrypted = [pow(int(num), d, N) for num in encrypted]
    return decrypted

def rsa_encrypt_decrypt():
    e = None
    N = None
    d = None
    text = None
    encrypted = None
    while True:
        print("Bitte wählen Sie den Modus: ")
        print("1: Berechnen Sie 'd' durch Primfaktorzerlegung von 'N'")
        print("2: Verschlüsseln Sie den Text mit RSA")
        print("3: Verschlüsseln Sie den Text mit RSA und entschlüsseln Sie ihn dann")
        print("4: Rechnen Sie Text in seine numerische Repräsentation um")
        print("5: Entschlüsseln Sie einen RSA-verschlüsselten Text")
        print("6: Wandeln Sie die numerische Repräsentation in Text um")
        mode = int(input("Ihre Wahl: "))

        if mode in [1] and e is None:
            e = int(input("Bitte geben Sie den Wert für 'e' ein: "))
        if mode in [2, 3] and e is None:
            e = int(input("Bitte geben Sie den Wert für 'e' ein: "))
        if mode in [1, 2, 3, 5] and N is None:
            N = int(input("Bitte geben Sie den Wert für 'N' ein: "))
        if mode in [5] and d is None:
            d = int(input("Bitte geben Sie den Wert für 'd' ein: "))
        if mode in [2, 3, 4, 6] and text is None:
            text = input("Bitte geben Sie den zu verarbeitenden Text ein: ")

        if mode == 1:
            d = calculate_d(e, N)
            print(f'd={d}')
        elif mode == 2:
            encrypted = encrypt_rsa(e, N, text)
            print(f'Encrypted={"|".join(map(str, encrypted))}')
        elif mode == 3:
            d = calculate_d(e, N)
            encrypted = encrypt_rsa(e, N, text)
            decrypted = decrypt_rsa(d, N, encrypted)
            print(f'Encrypted={"|".join(map(str, encrypted))}\nDecrypted={"|".join(map(str, decrypted))}')
        elif mode == 4:
            numbers = text_to_numbers(text)
            print(f'Numbers={"|".join(numbers)}')
        elif mode == 5:
            encrypted_input = input("Bitte geben Sie den verschlüsselten Text ein (im Format: 5409|2588|5409 etc.): ")
            encrypted = list(map(int, encrypted_input.split("|")))
            decrypted = decrypt_rsa(d, N, encrypted)
            print(f'Decrypted={"|".join(map(str, decrypted))}')
        elif mode == 6:
            numbers = text.split("|")
            print(f'Text={numbers_to_text(numbers)}')
        else:
            print('Invalid mode')

        again = input("Möchten Sie einen anderen Modus ausführen? (y/n): ")
        if again.lower() != 'y':
            break

rsa_encrypt_decrypt()
