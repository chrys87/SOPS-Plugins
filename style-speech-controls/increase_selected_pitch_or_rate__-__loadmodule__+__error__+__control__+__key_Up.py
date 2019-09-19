#! /usr/bin/python

# access the global orca speechserver
from orca import orca
from orca.speech import increaseSpeechPitch, increaseSpeechRate, increaseSpeechVolume
f = open("/tmp/orca-ratechanger", "r")
_param=f.read()
f.close()
if _param == "rate":
	increaseSpeechRate()
elif _param == "pitch":
	increaseSpeechPitch()
elif _param == "volume":
	increaseSpeechVolume()
