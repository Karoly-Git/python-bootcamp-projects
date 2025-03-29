import random

# ASCII Art for choices
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
choice_map = {'r': 0, 'p': 1, 's': 2}

user_choice = input("Choose rock (R), paper (P), or scissors (S): ").strip().lower()

if user_choice not in choice_map:
    print("Invalid choice! You lost. Game Over!")
else:
    user_index = choice_map[user_choice]
    pc_index = random.randint(0, 2)
    
    print("YOU:")
    print(options[user_index])
    print("PC:")
    print(options[pc_index])
    
    if user_index == pc_index:
        print("It's a tie! Play again.")
    elif (user_index == 0 and pc_index == 2) or (user_index == 1 and pc_index == 0) or (user_index == 2 and pc_index == 1):
        print("YOU won!")
    else:
        print("PC won!")
