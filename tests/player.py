""" Travis Ci Tests """
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hypixel
from dotenv import load_dotenv
import time

load_dotenv()
print(f"Test \"{os.path.basename(__file__)}\" is now running...\n")
try:
    API_KEY = os.environ['HY_API_KEY']
except KeyError:
    API_KEY = os.getenv("HY_API_KEY")
hypixel.setKeys([API_KEY])

player = hypixel.Player('hypixel') #This info should not change
playerinfo_json = player.getPlayerInfo()

assert playerinfo_json['uuid'] == 'f7c77d999f154a66a87dc4a51ef30d19'
assert player.getRank()['rank'] == 'Admin' #TODO make a function to get just rank
assert playerinfo_json['firstLogin'] == 1377123024367
print("\nDone! All tests finished.")
