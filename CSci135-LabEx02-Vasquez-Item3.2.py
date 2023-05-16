# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:46:37 2023

@author: jelly
"""

import random

possible_actions = ["rock", "paper", "scissors"]
name = input("Who dared to challenge me?: ")

computer_score = 0
player_score = 0
number_of_rounds = 0
game_running = True
 
print(f"Finally, a worthy oponent! {name.title()}")

number_of_rounds = int(input("How many times would you like to play?: "))
winning_score = number_of_rounds // 2 + 1

for round_count in range(1,number_of_rounds+1):
    
    print(f"Round {round_count}: So what is the your choice? (rock/paper/scissors):")
    
    player = input().lower()
    while player not in possible_actions:
        print ("Opps, your wrote the wrong words! only rock, paper, or scissors:")

        player = input().lower()
        computer = random.choice(possible_actions)

        print(f"\nplayer chose {player}, computer chose {computer}.\n")

        if player == computer:
            print ("Well, it's a tie!")
            if player == "rock" and computer == "scissors":
                print("Wow! You won!")
                player_score += 1
        elif player == "paper" and computer == "rock":
            print("Wow! You won!")
            player_score += 1
        elif player == "scissors" and computer == "paper":
            print ("Wow! You won!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

            print(f"Score: Player {player_score}; Computer {computer_score}\n")

        
    computer = random.choice(possible_actions)

    print(f"\nplayer chose {player}, computer chose {computer}.\n")

    if player == computer:
        print ("Well, it's a tie!")
        if player == "rock" and computer == "scissors":
            print("Wow! You won!")
            player_score += 1
    elif player == "paper" and computer == "rock":
        print("Wow! You won!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print ("Wow! You won!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

        print(f"Score: Player {player_score}; Computer {computer_score}\n")

      
    

if player_score == computer_score: 
    print(f"The game is tied {player_score}-{computer_score}. Try again {name.title()}!")
elif player_score > computer_score:
    print(f"You won the game {player_score}-{computer_score}. Congratulations {name.title()}!")
else:
    print(f"Opps Computer won the game {player_score}-{computer_score}. Better luck next time {name.title()}!")

