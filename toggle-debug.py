#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advanced plugin to toggle debugmode on/ off
#sopsproperty:loadmodule

import orca.orca
import orca.debug
import orca.speech
import orca.braille
import time
from subprocess import Popen

def outputMessage(Message):
    if (orca.settings.enableSpeech):
        orca.speech.speak(Message)
    if (orca.settings.enableBraille):
        orca.braille.displayMessage(Message)

if (orca.debug.debugLevel != orca.debug.LEVEL_ALL):
    if not orca.debug.debugFile:
        orca.debug.debugFile = open(time.strftime('debug-%Y-%m-%d-%H:%M:%S.out'), 'w')
    orca.debug.debugLevel = orca.debug.LEVEL_ALL
    orca.debug.eventDebugLevel = orca.debug.LEVEL_OFF
    outputMessage('Debugmode on')
else:
# reset doesnt work (why ever, as workarround start orca new)
#    orca.debug.debugLevel = orca.debug.LEVEL_OFF
#    outputMessage(str(orca.debug.debugLevel))
#    orca.debug.eventDebugLevel = orca.debug.LEVEL_OFF
#    if orca.debug.debugFile:
#    close(orca.debug.debugFile)
    p = Popen("orca --replace", shell=True)
    outputMessage('Debugmode off')
