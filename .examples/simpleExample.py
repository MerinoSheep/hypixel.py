""" This is an example of how you can use this API to create cool things.
    Just run this and you should see cool stuff. c:"""

import os, sys
from dotenv import load_dotenv

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import hypixel

load_dotenv()
API_KEYS = []
API_KEY = os.getenv("HY_API_KEY")
hypixel.set_keys(API_KEYS) # This sets the API keys that are going to be used.

Player = hypixel.Player('Snuggle') # This creates a Player-object and puts it to a variable called "Player".

PlayerName = Player.get_name() # This gets the player's name and puts it in a variable called "PlayerName". :3
print("Player is called ", end='')
print(PlayerName)

PlayerLevel = Player.get_level()
print(PlayerName + " is level: ", end='')
print(PlayerLevel) # This prints the level that we got, two lines up!

PlayerRank = Player.get_rank()
print(PlayerName + " is rank: ", end='')
print(PlayerRank['rank'])