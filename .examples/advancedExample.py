""" This is an example of how you can use this API to create cool things.
    Just run this and you should see cool stuff. c:"""

import os, sys
from dotenv import load_dotenv

currentdir = os.path.dirname(os.path.realpath(__file__)) # allows to import hypixel file for debugging purposes
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import hypixel
load_dotenv()
API_KEYS = []
API_KEY = os.getenv("HY_API_KEY")
hypixel.set_keys(API_KEYS) # This sets the API keys that are going to be used.

options = ['rank', 'level', 'karma', 'twitter','guild','guild members','quit']

while True:
    mahInput = input("\nPlease give me a Minecraft username/UUID: ")
    option_input = input(f"Please select from list: {options}\n> ").lower()
    player = hypixel.Player(mahInput) # Creates a hypixel.Player object using the input.

    try:
        if option_input == "rank": # If user selects rank,
            print("The player is rank: " + player.get_rank()['rank']) # Get the rank and print it.
            print(f"Were they previously a staff member? {player.get_rank()['wasStaff']}")

        elif option_input == "level":
            print("The player is level: " + str(player.get_level())) # Print the player's low level!

        elif option_input == "karma":
            print(f"The player has {player.JSON['karma']} karma.")

        elif option_input == "guild":
            print(f"Guild:{player.get_guild_ID()}")

        elif option_input == "guild members":
            guild_id = player.get_guild_ID()
            guild = hypixel.Guild(guild_id)
            guild_members = guild.get_members()
            print(guild_members)

        elif option_input == "twitter": # Okay this is a little more complicated
            try:
                socialMedias = player.JSON['socialMedia']['links'] # Check their social media
                print(socialMedias['TWITTER']) # And if they have a Twitter account, print it.
            except KeyError: # If an error comes up, saying they don't have a twitter account...
                print("This user doesn't have a Twitter account linked.")
        elif option_input == "quit":
            break
    except hypixel.PlayerNotFoundException: # If the player doesn't live on earth, catch this exception.
        print("Cannot find player. :/")
