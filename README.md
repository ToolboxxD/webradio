# flask_webradio

Check python version:

python --version


Virtual environments (shortened as "virtualenv") separate our new project’s Python dependencies from our other projects and from the Python libraries our operating system uses. If you don’t use a virtualenv, there’s a good chance you might break part of your OS. Start a new project with virtualenv:

    $ python -m venv webradio 

Alternative ist (not needed)

    $ pip install virtualenv

    $ virtualenv webradio

To begin using the virtual environment, it needs to be activate

    $ source webradio/bin/activate

 If you are done working in the virtual environment for the moment, you can deactivate it:

    $ deactivate

Once you have activated your programming environment, install Flask:

    $ pip install flask

first install a player on your system 

$ sudo apt-get update

$ sudo apt-get install mpd mpc

$ mpc add #linktostream
https://www.internet-radio.com/ link für streams in pls datei 

MPD wurde als unpraktisch empfungen 

pip install python-vlc

Install VLC Player
    $ sudo apt-get install vlc 

   Run the app:

$  python radio.py           