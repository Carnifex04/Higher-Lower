#importing modules
from replit import clear
from random import choice
from art import logo
from art import vs
from game_data import data

#printing logo and the relevant game rules
print(logo)
print("Welcome to the Higher Lower Game!!!")
print("The rules are simple: Given 2 choices, guess which one has more Instagram Followers :)")
print("The game ends when you make a wrong guess")

#taking input from player to start the game
start = input("Enter 'y' to start the game... ").lower()

#initializing a boolean variable to store the status of the game
wrong_answer = False

#initializing a variable to store the score of the player
score = 0

#function to compare the follower count of the two passed accounts
def compare(first_a, second_a):
  """Takes in two accounts as input and returns a boolean value depending on their followers"""

  user_choice = input("What do you think? Who has more followers on Instagram? Type 'A' or 'B': ").lower()
  if first_a["follower_count"] > second_a["follower_count"]:
    return user_choice == 'a'
  else:
    return user_choice == 'b'
  
#function for generating the second account from the list
def generating_second_account(first_a):
  """Takes input the first randomly generated account and returns a second random account"""
  second_a = choice(data)
  #condition for checking if both the accounts are the same
  while second_a == first_a:
    second_a = choice(data)
  return second_a

#function for printing the account details
def account_details(account, position):
  if position == 1:
    print("Compare A:", end = " ")
  else:
    print("Against B:", end = " ")
  
  print(account["name"] + ", " + account["description"] + ", from " + account["country"])

#initializing the first account
first_account = choice(data)

#checking condition to start the game
if start == 'y':
  while not wrong_answer:
    
    #clearing and printing the logo after every iteration
    clear()
    print(logo)

    #printing score if score is greater than 0
    if score > 0:
      print(f"You are right! Your current score is: {score}")
    
    #generating second account
    second_account = generating_second_account(first_account)

    #printint account details and the versus logo
    account_details(first_account, 1)
    print(vs)
    account_details(second_account,2)

    #comparing both the accounts
    #if true, increment the score and change the first_account to the second_account
    #else printing the exit statement, and exiting the loop
    if compare(first_account, second_account) == True:
      score+=1
      first_account = second_account
    else:
      clear()
      print(logo)
      print("Sorry, that's the wrong choice :(")
      print(f"Final Score: {score}")
      wrong_answer = True
    
    
  

  

