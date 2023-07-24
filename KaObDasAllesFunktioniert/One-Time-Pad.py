def encrypt_decrypt_vigenere(message, key, decrypt=False):
    result = ""
    key_length = len(key)

    for i in range(len(message)):
        char = message[i]
        offset = ord(key[i % key_length]) - ord('A')

        if decrypt:
            new_char = chr((ord(char) - ord('A') - offset) % 26 + ord('A'))
        else:
            new_char = chr((ord(char) - ord('A') + offset) % 26 + ord('A'))

        result += new_char

    return result


def calculate_key(plain_text, cipher_text):
    key = ""
    for i in range(len(plain_text)):
        plain_char = plain_text[i]
        cipher_char = cipher_text[i]

        offset = (ord(cipher_char) - ord(plain_char)) % 26
        key += chr(offset + ord('A'))

    return key


def main():
    mode = input("Geben Sie den Modus ein (e für Verschlüsselung, d für Entschlüsselung, k für Schlüsselberechnung): ").lower()

    if mode == "e" or mode == "d":
        message = input("Geben Sie die Nachricht ein, die Sie verschlüsseln / entschlüsseln möchten: ").upper()
        key = input("Geben Sie den Schlüssel ein, den Sie verwenden möchten: ").upper()
        result = encrypt_decrypt_vigenere(message, key, decrypt=(mode == "d"))

    elif mode == "k":
        plain_text = input("Geben Sie den Klartext ein: ").upper()
        cipher_text = input("Geben Sie das Chiffrat ein: ").upper()
        result = calculate_key(plain_text, cipher_text)

    else:
        print("Ungültiger Modus ausgewählt. Bitte wählen Sie 'e' zum Verschlüsseln, 'd' zum Entschlüsseln oder 'k' zur Schlüsselberechnung.")
        return

    print(f"\nErgebnis: {result}")


if __name__ == "__main__":
    main()
