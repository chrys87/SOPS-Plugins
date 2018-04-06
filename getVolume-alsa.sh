#!/bin/sh
# print the volume of the current alsa master
echo -n "Volume "
amixer sget Master | grep -o -m 1 '[[:digit:]]*%' | tr -d '%'
