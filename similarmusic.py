import pylast, re

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm
API_KEY = "e3d64479d574074eac7058d08de0dda7" # this is a sample key
API_SECRET = "063d322566d3a8bcbd48ac160aa5097a"

# In order to perform a write operation you need to authenticate yourself
username = "mayuroks"
password_hash = pylast.md5("hydrofuran")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)


######### define a track ######
track = network.get_track("rihanna", "umbrella")
#track.love()
#track.add_tags(("awesome", "favorite"))

# type help(pylast.LastFMNetwork) or help(pylast) in a python interpreter to get more help
# about anything and see examples of how it works

########### MY CODE ###########
my_list = track.get_similar()
song = [str(my_list[i][0]) for i in range(len(my_list))] ##songs = lists of songs(string)
print(str(my_list[10][0]), "yaya")
print(song[:10])









