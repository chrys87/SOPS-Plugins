#! /usr/bin/python

#
# Copyright 2019, F123 Consulting, <information@f123.org>
# Copyright 2019, Michael Taboada, <michael@michaels.world>
# Copyright 2019, Informal Informática, <gestao@informal.com.br>
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3, or (at your option) any later
# version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this package; see the file COPYING.  If not, write to the Free
# Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

# access the global orca speechserver
from orca import orca
from orca.speech import increaseSpeechPitch, increaseSpeechRate, increaseSpeechVolume
try:
        f = open("/tmp/orca-ratechanger", "r")
        _param=f.read()
        f.close()
except FileNotFoundError:
        _param="volume"
if _param == "rate":
	increaseSpeechRate()
elif _param == "pitch":
	increaseSpeechPitch()
elif _param == "volume":
	increaseSpeechVolume()
