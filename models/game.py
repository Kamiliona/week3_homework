import random

first_choice = input("Rock, Paper or Scissors? ").lower() 
while first_choice != "rock" and first_choice != "paper" and first_choice !="scissors":
  first_choice = input("Say what? try again: ").lower()

second_choice = input("Rock, Paper or Scissors? ").lower()

# random_num = random.randint(0,2)
# if random_num == 0:
#   second_choice = "rock"
# elif random_num == 1:
#   second_choice = "paper"
# elif random_num == 2:
#   second_choice = "scissors"


print("Your choice:", first_choice)
print("Other player's choice:", second_choice)
print()

if first_choice == "rock":
  if second_choice == "rock":
    print("and the winner is ... my therpaist, try again!")
  elif second_choice == "paper":
    print("Not today amigo!")
  elif second_choice == "scissors":
    print("chicken, dinner I guess you are a winner")
elif first_choice == "paper":
  if second_choice == "paper":
    print("and the winner is ... my therpaist, try again!")
  elif second_choice == "scissors":
    print("Not today amigo!")
  elif second_choice == "rock":
    print("chicken, dinner I guess you are a winner")
elif first_choice == "scissors":
  if second_choice == "scissors":
    print("and the winner is ... my therpaist, \n try again!")
  elif second_choice == "rock":
    print("Not today amigo!")
  elif second_choice == "paper":
    print("chicken, dinner I guess you are a winner?")
