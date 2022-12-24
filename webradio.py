#!/usr/bin/python
# -*- coding: utf-8 -*-
# python --version 3.9.2

from flask import Flask
from flask import render_template
from flask import request
from predefines import host, port, txtFile, templateFile
from predefines import isInteger, mpcCommand
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])    
def hello_world(name='McGreg FM',volume =50): #volume =50
    # get file pointer to sender list
    stations = []
    stationURLs = []
    stationOutput = ''

    for x in open('stations.txt','r'):
	    a = x.split("|")
	    stations.append(a[0])
	    stationURLs.append(a[1].strip())

    #controle mpc 
    if request.method == 'POST':
        if request.form['submit'] == 'turn radio on':
            mpcCommand(['mpc', 'play'])
        elif request.form['submit'] == 'turn radio off':
            mpcCommand(['mpc', 'stop'])
        elif request.form['submit'] == 'change':
            mpcCommand(['mpc', 'play', str(request.form['station'])])
        elif request.form['submit'] == '+5':
            mpcCommand(['mpc', 'volume', '+5'])
        elif request.form['submit'] == '-5':
            mpcCommand(['mpc', 'volume', '-5'])
        elif request.form['submit'] == 'update playlist':
            mpcCommand(['mpc', 'clear'])
            for stationURL in stationURLs:
                mpcCommand(['mpc', 'add', stationURL])
            
        #show queue track nummer
        #cmd=['mpc', '-f', '%position%']
        #p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        #position = p.stdout.read()

        position = mpcCommand(['mpc', '-f', '%position%'])
        #print(position.decode('utf8').split('['))
        #   ['2\n', 'playing] #2/6   0:11/0:00 (0%)\nvolume: 47%   repeat: off   random: off   single: off   consume: off\n']
        idx = position.decode('utf8').split('[')
        position = idx[0].strip()
        #print(position)

        if isInteger(position) == False:
            position = 0
        x = 1
        for station in stations:
            stationOutput += '<option value="' + str(x) + '" '
            if x == int(position):
                stationOutput += 'selected="selected"'
            stationOutput += '>' + station + '</option>'
            x += 1            
        
        
    volume = mpcCommand(['mpc', 'volume'])    
    #print('Volume'+ str(volume))
    return render_template(templateFile, name=name, stations=stationOutput.strip(), volume=volume)    

if __name__ == '__main__': 
    app.run(host=host, port=port, debug=True)	