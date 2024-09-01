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

# Write your code below this line 👇
game_image = [rock, paper, scissors]
game_image_length = len(game_image)

print("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors!")
user_choice = int(input())

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_image[user_choice])

    print("Computer Chose:")
    computer_choice = random.randint(0, game_image_length - 1)
    print(game_image[computer_choice])
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    elif (user_choice == 0 and computer_choice == 0) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2):
        print("Draw!")
    else:
        print("You Lose!")
