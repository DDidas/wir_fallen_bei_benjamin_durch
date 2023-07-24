
def erweiterter_ggt(a, b):
    """Berechnet den größten gemeinsamen Teiler zweier Zahlen a und b
    und gibt zusätzlich die Koeffizienten s und t zurück, so dass
    s*a + t*b = ggt(a,b) gilt."""
    if a == 0:
        return b, 0, 1
    else:
        ggt, s, t = erweiterter_ggt(b % a, a)
        return ggt, t - (b // a) * s, s


def multiplative_inverse(a, b):
    ggt, s, _ = erweiterter_ggt(a, b)
    if ggt != 1:
        return None
    else:
        return s % b


if __name__ == '__main__':
    print(erweiterter_ggt(27, 85))
    print(multiplative_inverse(27, 85))



def symetrische_verschluesselung(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Konvertiere den Buchstaben in einen entsprechenden Integer-Wert (A=0, B=1, usw.)
            char_value = ord(char.upper()) - ord('A')
            # Verschlüssele den Integer-Wert mit dem Verschiebeschlüssel
            encrypted_value = (char_value + shift) % 26
            # Konvertiere den verschlüsselten Integer-Wert zurück in einen Buchstaben
            encrypted_char = chr(encrypted_value + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == '__main__':
    encrypted_text = symetrische_verschluesselung("AVEYRON", 11)
    print("Verschlüsselter Text:", encrypted_text)


def vigenere_encryption(plaintext, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Konvertiere den Buchstaben in einen entsprechenden Integer-Wert (A=0, B=1, usw.)
            char_value = ord(char.upper()) - ord('A')
            # Konvertiere den Buchstaben des Schlüsselworts in einen entsprechenden Integer-Wert
            keyword_char_value = ord(keyword[i % keyword_length]) - ord('A')
            # Verschlüssele den Buchstaben mit dem Schlüsselwort
            encrypted_value = (char_value + keyword_char_value) % 26
            # Konvertiere den verschlüsselten Integer-Wert zurück in einen Buchstaben
            encrypted_char = chr(encrypted_value + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == '__main__':
    # Beispielaufruf des Algorithmus mit dem Text "HELLO" und dem Schlüsselwort "KEY"
    plaintext = "AVEYRON"
    keyword = "FRZ"
    encrypted_text = vigenere_encryption(plaintext, keyword)
    print("Verschlüsselter Text:", encrypted_text)

def findTripel(wert1, wert2, wert3, Gesamtwert):
    count = 0
    xBereich = Gesamtwert // wert1
    yBereich = Gesamtwert // wert2
    zBereich = Gesamtwert // wert3

    for b in range(1,
                   xBereich):  # Der Wertebereich von b basiert auf der maximalen Anzahl der Bücher, die mit dem Budget von gesamtwert gekauft werden können
        for p in range(1, yBereich):  # Der Wertebereich von p basiert auf der maximalen Anzahl der Pralinenschachteln
            for w in range(1, zBereich):  # Der Wertebereich von w basiert auf der maximalen Anzahl der Weinflaschen
                if wert1 * b + wert2 * p + wert3 * w == Gesamtwert:
                    count += 1
                    print("Tripel " + str(count) + ": " + str(b) + " Bücher, " + str(p) + " Pralinenschachteln, " + str(
                        w) + " Weinflaschen")

    print(count)


if __name__ == '__main__':
    print(findTripel(11, 5, 8, 250))

