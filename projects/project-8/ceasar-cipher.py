ascii_logo = """
  ______             __         __  __
 |  ____|           /_/        |  \/  |
 | |__ _ __ __ _     ___ _ __ | \  / | __ _ ___
 |  __| '__/ _` |   / _ \ '_ \| |\/| |/ _` / __|
 | |____ | | (_| |  |  __/ | | | |  | | (_| \__ \
 |______|_| \__,_|   \___|_| |_|_|  |_|\__,_|___/
"""

print(ascii_logo)

characters = "U5*,X~'ZK6{x02iyz[WQ:fp<M>HEwqhLOrPBt]}@3svTD.8lSG(4gNRC#d_A$+-e|?I^79&\"1;Y=V/ku)n!omJbFcaj"

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(text, direction, shift):
    new_text = ""
    for char in text:
        if char in characters:  # Check if the character is in the characters
            index_of_char = characters.index(char)

            if direction == 'e':
                new_index = (index_of_char + shift) % len(characters)  # Modulo wrapping
            else:
                new_index = (index_of_char - shift) % len(characters)

            new_text += characters[new_index]
        else:
            new_text += char

    return new_text

print('Encrypted text:', encrypt(text, direction, shift))
