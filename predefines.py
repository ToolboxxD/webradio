import subprocess 
from subprocess import Popen, PIPE

host = '0.0.0.0'
port = 1234
txtFile = 'stations.txt'
templateFile = 'interface.html'
def isInteger(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

