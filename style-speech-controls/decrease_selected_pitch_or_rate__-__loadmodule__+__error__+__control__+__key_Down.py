#! /usr/bin/python

# access the global orca speechserver
from orca import orca
from orca.speech import decreaseSpeechPitch, decreaseSpeechRate, decreaseSpeechVolume
try:
        f=open("/tmp/orca-ratechanger", "r")
        _param=f.read()
        f.close()
except FileNotFoundError:
        _param="volume"
if _param == "rate":
	decreaseSpeechRate()
elif _param == "pitch":
	decreaseSpeechPitch()
elif _param == "volume":
	decreaseSpeechVolume()
