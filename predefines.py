import subprocess

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

def mpcCommand(cmd):
	p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	pOutput = p.stdout.read()
	print('inMpcCommand ' + str(pOutput))
	return	pOutput