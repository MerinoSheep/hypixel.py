""" Travis Ci Tests """
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hypixel
from dotenv import load_dotenv
load_dotenv()

print(f"Test \"{os.path.basename(__file__)}\" is now running...\n")

API_KEY = os.getenv("HY_API_KEY")
hypixel.set_keys([API_KEY])

player = hypixel.Player('hypixel') #This info should not change
playerinfo_json = player.get_player_info()

assert playerinfo_json['uuid'] == 'f7c77d999f154a66a87dc4a51ef30d19'
assert player.get_rank()['rank'] == 'Admin' #TODO make a function to get just rank
assert playerinfo_json['firstLogin'] == 1377123024367

network_info = hypixel.Network()
response = network_info.key_info()
print("\nDone! All tests finished.")
