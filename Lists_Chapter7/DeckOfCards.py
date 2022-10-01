# Create a deck of cards
deck = [x for x in range(0, 52)]
print("Created deck:")
print(deck)

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
      "10", "Jack", "Queen", "King"]
        
# Shuffle the cards
import random
random.shuffle(deck)
print("Shuffled deck:")
print(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card # [",i, "] Card number", deck[i], "is", rank, "of", suit)
    print("\t Suits length", len(suits), " ranks lenghth ", len(ranks))
    
    
suits.append("Cooper")
print("Adding Cooper to our suits")
print("\t Suits length", len(suits), " ranks lenghth ", len(ranks))
    
