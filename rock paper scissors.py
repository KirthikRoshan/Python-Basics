# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:51:19 2023

@author: KirthikRoshan
"""
print("\nWelcome to the Game. My name is “RoPaSc” Gamer\n")
num = int(input("\nEnter number of attempts:\n",))
#print(num)
name = str(input("\nEnter your name:\n",))
#print(name)
user = []
computer = []


  
import random

i = 1
while i < num+1:
  
    
  
    user_action = input("\nShow your Hand (rock, paper, scissors): \n")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n{name} chose {user_action}, computer chose {computer_action}.\n")
    
    if user_action == computer_action:
        print(f"\nBoth players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"\nRock smashes scissors! {name} win!")
            user.append(1)
        else:
            print(f"\nPaper covers rock! {name} lose.")
            computer.append(1)
         
            
    elif user_action == "paper":
        if computer_action == "rock":
            print(f"\nPaper covers rock! {name} win!")
            user.append(1)
        else:
            print(f"\nScissors cuts paper! {name} lose.")
            computer.append(1)
            
             
    elif user_action == "scissors":
        if computer_action == "paper":
            print(f"\nScissors cuts paper! {name} win!")
            user.append(1)
        else:
            print(f"\nRock smashes scissors! {name} lose.")
            computer.append(1)
    #print(f"\nCur Score: {name} - {len(user)}; Computer - {len(computer)}\n")
    i += 1 
    print(f"\n Round {i-1} Score: {name} - {len(user)}; Computer - {len(computer)}\n")   
   
    
   
#print(f"\nnumber of times {name} won :",len(user))
#print("\nnumber of times computer won :",len(computer))
print(f"\nFinal Score: {name} - {len(user)}; Computer - {len(computer)}\n")
if (len(user) > len(computer)):
    print(f"\nCongratulations {name}, you won the game! Sorry, computer, you lost.")
elif (len(user) == len(computer)):
    print(f"\nCongratulations {name} and computer, you tied the game!.")
else:
    print(f"\nCongratulations Computer, you won the game! Sorry, {name}, you lost.")

        
        