#pre conditions:
#sudo apt-get install vlc
#pip install python-vlc

import vlc
from time import sleep

url = 'http://streams.radiobob.de/bob-live/mp3-192/mediaplayer'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
player.play()

sleep (2)
while player.is_playing():
    sleep(1)

print("Player Stop\n")
player.stop()