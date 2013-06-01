import requests, re
def download_music(songname):
  """to call this func : download_music( artist - song )

for eg: download_music('rihanna - umbrella')"""

  na = songname.split(' ')
  na.remove('-')
  na = '_'.join(na)
  search_url = 'http://www.mrtzcmp3.net/' + na + '_1s.html'
  print('NAME : ', search_url)
  hdr = {'user-agent':'EqxuinoX/2.5'}

  r = requests.get(search_url, headers = hdr)
  match = re.search('D\?.*?_', r.text)    ## REGEX to get ID of download
  match.group(0)[2:-1]       ## ID first download
  dl_url = 'http://www.mrtzcmp3.net/' + match.group(0)[2:-1] + '.mrtzcmp3'
  print('NAME : ', dl_url)

  ## utilizing cookie from search here
  ne = requests.get(dl_url, headers=hdr, cookies=r.cookies)

  ## SAVING TO FILE song_name.mp3

  songname = songname + ".mp3"
  mp3 =  open(songname, 'wb+')         # change owner n permissions of the file etc
  mp3.write(ne.content)
  mp3.close()

#download_music('snow patrol - chasing cars')
#download_music('Waiting Here for You - (Night Music Edit)')
#print(download_music.__doc__)
#download_music('hoodie allen - hey now')


