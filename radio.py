#!/usr/bin/python
# -*- coding: utf-8 -*-
# python --version 3.10.6

from flask import Flask
from flask import render_template
from flask import request
import vlc
from time import sleep
from predefines import host, port, txtFile, templateFile
from predefines import isInteger
import subprocess

app = Flask(__name__)

class vlcMyPlayer:
    #define VLC instance
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
    
    #Define VLC player
    player = instance.media_player_new()

    def vlcStartRadioStream(self, stationUrl):
        #Define VLC media
        if stationUrl==0:
            stationUrl = 'http://streams.radiobob.de/bob-live/mp3-192/mediaplayer'
        media=self.instance.media_new(stationUrl)

        #Set player media
        self.player.set_media(media)

        #Play the media
        self.player.play()

        #need sleep bigger 2 to start 
        sleep (5)
        print("Vol start = "+str(self.player.audio_get_volume()))

    def vlcStopRadioStream(self):
        self.player.stop()    

    def vlcVolume(self):
        curVol = -1
        curVol= self.player.audio_get_volume()
        if curVol == -1:
            curVol = 'Radio not playing'
        return curVol
    
    def vlcVolumePlus(self, value):
        curVolplus= self.player.audio_get_volume()
        value = curVolplus + value
        
        self.player.audio_set_volume(value)
        return value

    def vlcVolumeMinus(self, value):
        curVolmin= self.player.audio_get_volume()
        value = curVolmin - value
        self.player.audio_set_volume(value)
        return value

@app.route('/', methods=['GET', 'POST'])    
def webradio(name='McGreg FM'): 
    # get file pointer to sender list
    stations = []
    stationURLs = []
    stationOutput = ''
    
    for x in open('stations.txt','r'):
        a = x.split("|")
        stations.append(a[0])
        stationURLs.append(a[1].strip())

    #create VLC instance
    player = vlcMyPlayer()
    
    #get an check volume
    volume = player.vlcVolume()
    if request.method == 'POST':
        if request.form['submit'] == 'turn radio on':
            player.vlcStartRadioStream(0)
        elif request.form['submit'] == 'turn radio off':
            player.vlcStopRadioStream()
            #print("Off\n")
        elif request.form['submit'] == '+5':
            volume = player.vlcVolumePlus(5)
            #print("Vol+ ="+str(volume))
        elif request.form['submit'] == '-5':
            volume = player.vlcVolumeMinus(5)
            #print("Vol- ="+str(volume))
        elif request.form['submit'] == 'change':
            selectedIndex = stations.index(str(request.form['station']))
            urlIndex = stationURLs[selectedIndex]
            player.vlcStartRadioStream(urlIndex)   

    volume = player.vlcVolume()
    return render_template(templateFile, name=name, stations=stations, volume=volume)    

if __name__ == '__main__': 
    app.run(host=host, port=port, debug=True)