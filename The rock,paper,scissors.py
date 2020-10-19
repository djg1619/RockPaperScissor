#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

choices = ['Rock', 'Paper', 'Scissors']
opponent = random.choice(choices)

def intro():
    print("Welcome to Dwayne 'The Rock' Johnson, Paper, Scissors")
    print('\nThe computer has already selected their move!')
    print('Please type R for Rock, P for Paper and S for Scissors')    
    
def player_choice(player):
    if player.lower().startswith('r'):
        player = 'Rock'
    if player.lower().startswith('p'):
        player = 'Paper'
    if player.lower().startswith('s'):
        player = 'Scissors'
    return player

def cadence():
    print('ROCK!')
    time.sleep(1)
    print('PAPER!')
    time.sleep(1)
    print('SHOOT!')
    time.sleep(1)
    
def win_condition(opponent, player):
    if opponent == 'Paper' and player == 'Paper':
        print('Draw!')
    if opponent == 'Scissors' and player == 'Scissors':
        print('Draw!')
    if opponent == 'Rock' and player == 'Rock':
        print('Draw!')
    if opponent == 'Rock' and player == 'Scissors':
        print('You have lost!')
    if opponent == 'Paper' and player == 'Rock':
        print('You have lost!')
    if opponent == 'Scissors' and player == 'Paper':
        print('You have lost!')      
    if player == 'Rock' and opponent == 'Scissors':
        print('You have won!')
    if player == 'Paper' and opponent == 'Rock':
        print('You have won!')
    if player == 'Scissors' and opponent == 'Paper':
        print('You have won!')
        
def replay():
    return input('Would you like to play again?:y or n').lower().startswith('y')
#Gameplay loop
while True:
    intro()
    opponent = random.choice(choices)
    player = player_choice(input("\nNow pick! Dwayne 'The Rock' Johnson, Paper or Scissors: "))
    print('you have picked ' + player)
    cadence()
    print('your opponent picked ' + opponent)
    time.sleep(1)
    win_condition(opponent, player)
    if not replay():
        break


# In[ ]:


print(opponent)


# In[ ]:


def play_game():
    game_on = input('Would you like to play the game?: y or n').lower()
    if game_on == 'y' or game_on == 'yes':
        game_on = True
        return game_on
    if game_on == 'n' or game_on == 'no':
        game_on = False
        return game_on


# In[ ]:




