logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = {}

# Suits and Symbols
suits = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Clubs": "♣",
    "Spades": "♠"
}

# Numbered Cards (2-9)
for num in range(2, 10):
    cards[str(num)] = {}
    for suit, symbol in suits.items():
        cards[str(num)][suit] = rf"""        
.------.
|{num:<2}    |
|      |
|  {symbol}   |
|    {num:>2}|
'------'     
"""

# Ace
cards["Ace"] = {}
for suit, symbol in suits.items():
    cards["Ace"][suit] = rf"""        
.------.
|A     |
|  {symbol}   |
|      |
|     A|
'------'     
"""

# Face Cards
face_cards = {
    "Jack": "J",
    "Queen": "Q",
    "King": "K"
}

for face, letter in face_cards.items():
    cards[face] = {}
    for suit, symbol in suits.items():
        cards[face][suit] = rf"""        
.------.
|{letter} /\  |
| /  \ | 
| {symbol}  {symbol} |
|  \/ {letter}|
'------'     
"""
