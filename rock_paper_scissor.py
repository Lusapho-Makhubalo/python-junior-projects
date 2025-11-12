import random

choices = ('r', 'p', 's')
user_choice = input("Enter your choice (Rock, Paper, Scissors? (r/p/s): ").lower()
if user_choice not in choices:
 print("Invalid choice!")
computer_choice = random.choice(choices)
if user_choice == "r":
  print("")
print(f'You chose {user_choice}')