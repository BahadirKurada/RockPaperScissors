import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


computer = random.randint(0,2)
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player == 0:
    print(rock)
    if computer == 0 and player == 0:
        print(f"Computer chose:\n{rock}")
        print("It's a draw")
    elif computer == 1 and player == 0:
        print(f"Computer chose:\n{paper}")
        print("You lose")
    elif computer == 2 and player == 0:
        print(f"Computer chose:\n{scissors}")
        print("You win!")
elif player == 1:
    print(paper)
    if computer == 0 and player == 1:
        print(f"Computer chose:\n{rock}")
        print("You Win!")
    elif computer == 1 and player == 1:
        print(f"Computer chose:\n{paper}")
        print("It's a draw")
    elif computer == 2 and player == 1:
        print(f"Computer chose:\n{scissors}")
        print("You lose")
else:
    print(scissors)
    if computer == 0 and player == 2:
        print(f"Computer chose:\n{rock}")
        print("You lose")
    elif computer == 1 and player == 2:
        print(f"Computer chose:\n{paper}")
        print("You win!")
    elif computer == 2 and player == 2:
        print(f"Computer chose:\n{scissors}")
        print("It's a draw")



