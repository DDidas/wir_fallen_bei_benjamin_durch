'''
Created on 15.11.2021

@author: Ramona Glötter
'''

# Quelle der Wörter: https://de.wikipedia.org/wiki/Liste_der_h%C3%A4ufigsten_W%C3%B6rter_der_deutschen_Sprache

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
    
def decode_with_key(text, text_new, caesar):
    
    while(int(caesar) <= 0 or int(caesar) > 26):
        print("Verschiebung nicht möglich, da der Parameter ungültig ist.")
        caesar = input("Um wie viele Stellen soll der Text verschoben werden ?? ")
        
    caesar = 26 - int(caesar)
    text_new = shift(text, caesar)
    print("\nEntschlüsselter Text: ")
    print(text_new)
    
def decode(text, text_new, caesar):
    
    wortspeicher = open("wortspeicher.txt", "r")
    
    test = 0
    text_new = shift(text, caesar)
    
    counter = 0
    word = wortspeicher.readline(counter)
    
    while (word != ":wq!"):
        if (word in text_new or word.lower() in text_new):
            test += 1
        counter += 1
        word = wortspeicher.readline(counter)
        
    if (test >= 2):
        print("\nEntschlüsselter Text: ")
        print(text_new)
    else:
        if (caesar > -26):
            caesar = caesar - 1
            text_new = shift(text, caesar)
            decode(text, text_new, caesar)
        else:
            print("Der Text konnte nicht entschlüsselt werden :(")
        
def shift(text, caesar):
    
    text_new = ""
    
    for i in text:
        ascii = ord(i)
        if(ascii < 65 or ascii > 90 and ascii < 97 or ascii > 122):
            text_new = text_new + chr(ascii)
        else:
            character_new = int(ascii) + int(caesar)
            if(character_new < 65):                             # Buchstabe kleiner als A = 65
                rest = 65 - character_new
                text_new += chr(91 - rest)
            elif(character_new > 90 and ascii <= 90):           # Buchstabe ist zwischen Z = 90 und a = 97, aber groß
                rest = character_new - 90
                text_new += chr(64 + rest)
            elif(character_new < 97 and ascii >= 97):           # Buchstabe ist zwischen Z = 90 und a = 97, aber klein
                rest = 97 - character_new
                text_new += chr(123 - rest)
            elif(character_new > 122):                            # Buchstabe größer als z = 122
                rest = character_new - 122
                text_new += chr(96 + rest)
            else:
                text_new += chr(character_new)
        
    return (text_new)

def vigenere(key, text, text_new):
    
    counter = 0
    
    for letter in text:
        if (ord(letter) >= 65 and ord(letter) <= 90 or ord(letter) >= 97 and ord(letter) <= 122):
            key_letter = key[counter]
            letter_new = shift_vigenere(letter, key_letter)
            text_new += letter_new
            if (counter < len(key) - 1):
                counter += 1
            else:
                counter = 0
        else:
            text_new += letter
            
    print(text_new)
    return (text_new)

def shift_vigenere(letter, key_letter):
    
    if (ord(letter) <= 90):                         # Großbuchstaben: 65-90
        key_letter = key_letter.upper()
        distance = ord(letter) - 65
        new_character = ord(key_letter) + distance
        if (new_character > 90):
            rest = new_character - 90
            letter_new = chr(65 + rest - 1)
        else:
            letter_new = chr(new_character)
    else:                                               # Kleinbuchstaben: 97-122
        distance = ord(letter) - 97
        new_character = ord(key_letter) + distance
        if (new_character > 122):
            rest = new_character - 122
            letter_new = chr(97 + rest - 1)
        else:
            letter_new = chr(new_character)
    
    return (letter_new)

def main():
    
    wahl = input("Welche Verschlüsselung soll angewendet werden (Caesar/Vigenere) ?? ")
    
    if (wahl == "Caesar" or wahl == "caesar"):
        code = input("Soll dein Text verschlüsselt werden (ja/nein) ?? ")
        text = input("Gib einen Text ein: ")
        text_new = ""
        
        if (code == "Ja" or code == "ja"):
            caesar = input("Um wie viele Stellen soll der Text verschoben werden ?? ")
            text_without_special = specials(text)
            encode(text_without_special, text_new, caesar)
        elif (code == "Nein" or code == "nein"):
            known_key = input("Ist der Schlüssel bekannt (ja/nein) ?? ")             # Herausfinden, ob der Schlüssel bekannt ist
            if (known_key == "Ja" or known_key == "ja"):
                caesar = input("Bitte gib den Schlüssel ein: ")
                decode_with_key(text, text_new, caesar)
            elif (known_key == "Nein" or known_key == "nein"):
                caesar = 0
                decode(text, text_new, caesar)
            else:
                print("Die Eingabe ist ungültig")
        else:
            print("Die Eingabe ist ungültig.")
    elif (wahl == "Vigenere" or wahl == "vigenere"):
        check = 1
        key = " "
        while (key == "" or len(key) < 2 or check == 0):      # Eingabe des Schlüsselwortes wird überprüft
            check = 1
            for letter in key:
                if (ord(letter) >= 65 and ord(letter) <= 90 or ord(letter) >= 97 and ord(letter) <= 122):   # Wenn eine Eingabe kein Buchstabe ist (Großbuchstaben: 65-90, Kleinbuchstaben: 97-122)
                    check = 1
                else:
                    print("Das Schlüsselwort muss mindestens 2 Zeichen haben und darf keine Ziffern oder Sonderzeichen enthalten.")
                    key = input("Lege ein Schlüsselwort fest: ")
                    check = 0
                    break
        
        text = input("Gib einen Text ein: ")
        text_new = ""
        key = key.lower()
        text_without_special = specials(text)
        vigenere(key, text_without_special, text_new)
    else:
        print("Die Eingabe ist ungültig.")
    
if __name__ == '__main__':
    main()





