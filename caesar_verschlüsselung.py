
def specials(text):

    text_without_special = ""

    for letter in text:
        if (letter == "ä"):
            text_without_special += "ae"
        elif (letter == "ö"):
            text_without_special += "oe"
        elif (letter == "ü"):
            text_without_special += "ue"
        elif (letter == "ß"):
            text_without_special += "ss"
        else:
            text_without_special += letter

    return text_without_special

def encode(text, text_new, caesar):

    while(int(caesar) < -26 or int(caesar) > 26):
        print("Verschiebung nicht möglich, da der Parameter ungültig ist.")
        caesar = input("Um wie viele Stellen soll der Text verschoben werden ?? ")

    text_new = shift(text, caesar)
    print("\nVerschlüsselter Text: ")
    print(text_new)

def shift(text, caesar):

    text_new = ""

    for i in text:
        ascii = ord(i)
        if(ascii < 65 or ascii > 90 and ascii < 97 or ascii > 122):
            text_new = text_new + chr(ascii)
        else:
            character_new = int(ascii) + int(caesar)
            if(character_new < 65):                     # Buchstabe kleiner als A = 65
                rest = 65 - character_new
                text_new += chr(91 - rest)
            elif(character_new > 90 and ascii <= 90):   # Buchstabe ist zwischen Z = 90 und a = 97, aber groß
                rest = character_new - 90
                text_new += chr(64 + rest)
            elif(character_new < 97 and ascii >= 97):   # Buchstabe ist zwischen Z = 90 und a = 97, aber klein
                rest = 97 - character_new
                text_new += chr(123 - rest)
            elif(character_new > 122):                    # Buchstabe größer als z = 122
                rest = character_new - 122
                text_new += chr(96 + rest)
            else:
                text_new += chr(character_new)

    return (text_new)

def main():

    text = input("Gib einen Text ein: ")
    caesar = input("Um wie viele Stellen soll der Text verschoben werden ?? ")
    text_without_special = specials(text)
    text_new = ""
    encode(text_without_special, text_new, caesar)

if __name__ == '__main__':
    main()