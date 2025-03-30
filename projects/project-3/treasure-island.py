print("Welcome to the enchanted Treasure Island!")
print("Your mission is to find the legendary treasure hidden deep within the island... but beware... danger lurks at every corner.", 3)

# Asking the user which direction they want to go
direction = input("The wind whispers... Do you want to go left or right? Type 'left' or 'right': ").lower()

# Check if they chose the correct direction
if direction != 'left':
    print("The ground beneath you trembles... You fall into a dark pit and disappear into the unknown. Game Over!", 4)
else:
    # Asking the user what they want to do next
    action = input("You stand before a wild river. The current is strong. Do you want to swim or wait for a boat? Type 'swim' or 'wait': ").lower()
    
    if action != 'wait':
        print("The river is too powerful! A crocodile lunges at you from the depths... You are its next meal. Game Over!", 4)
    else:
        # Asking the user which door they want to choose
        print("A mysterious house emerges from the fog. Three doors stand before you—red, blue, and yellow. Which one will you choose?", 3)
        door_color = input("Type 'red', 'blue', or 'yellow': ").lower()
        
        if door_color == 'yellow':
            print("The golden door creaks open and inside you find the treasure chest... shimmering with riches! You've found the treasure. You win!", 4)
        else:
            if door_color == "red":
                print("The door opens to reveal a blazing inferno. The heat is unbearable. You are consumed by the flames. Game Over!", 4)
            elif door_color == 'blue':
                print("You step into a room filled with growls. Out of the shadows, wild beasts pounce on you. You have been devoured. Game Over!", 4)
            else:
                print(f"The {door_color} door seems to vanish before your eyes. You stand there, confused, and then the ground opens up beneath you. Game Over!", 4)
