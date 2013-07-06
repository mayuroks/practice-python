import pylast, re
def similar_search(artist, song):
  '''USAGE : similar_search('rihanna', 'umbrella')
  OUTPUT is a LIST passed to thread-pool manager
  which will decide the rate of download, assign download_music threads etc'''
  # You have to have your own unique two values for API_KEY and API_SECRET
  # Obtain yours from http://www.last.fm/api/account for Last.fm
  API_KEY = "e3d64479d574074eac7058d08de0dda7" # this is a sample key
  API_SECRET = "063d322566d3a8bcbd48ac160aa5097a"

  # In order to perform a write operation you need to authenticate yourself
  username = "XXXXX"
  password_hash = pylast.md5("XXXXX")

  network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

  ######### define a track ######
  #track = network.get_track("rihanna", "umbrella")
  track = network.get_track(artist, song)

  print(track.get_name)

  ########### MY CODE ###########
  my_list = track.get_similar()
  song_list = [(my_list[i][1], str(my_list[i][0])) for i in range(len(my_list))]
  song_list = sorted(song_list, reverse=True)
  #print(song_list[:10][8][1])
  print(song_list[:10])
  result = []
  [result.append(i[1]) for i in song_list]
  print('RESULT SNAP : ', result[:20])
  return result

# print(similar_search.__doc__)
# similar_search('tycho', 'past is prologue')
