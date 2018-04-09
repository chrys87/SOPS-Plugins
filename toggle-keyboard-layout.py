#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advanced plugin to toggle keyboard leyout
#sopsproperty:loadmodule

import orca.orca
import orca.settings
import orca.speech
import orca.braille

def outputMessage(Message):
	if (orca.settings.enableSpeech):
		orca.speech.speak(Message)
	if (orca.settings.enableBraille):
		orca.braille.displayMessage(Message)

if orca.settings.keyboardLayout == orca.settings.GENERAL_KEYBOARD_LAYOUT_LAPTOP:
    orca.settings.keyboardLayout = orca.settings.GENERAL_KEYBOARD_LAYOUT_DESKTOP
    orca.settings.orcaModifierKeys = orca.settings.DESKTOP_MODIFIER_KEYS
    outputMessage('Desktop Layout')
else:
    orca.settings.keyboardLayout = orca.settings.GENERAL_KEYBOARD_LAYOUT_LAPTOP
    orca.settings.orcaModifierKeys = orca.settings.LAPTOP_MODIFIER_KEYS
    outputMessage('Laptop Layout')

