#! /bin/bash

[ -f /tmp/orca-ratechanger ] && contents=$(cat /tmp/orca-ratechanger) || contents="rate"
case "$contents" in
    rate)
	contents="pitch"
	;;
    pitch)
	contents="volume"
	;;
    volume)
	contents="rate"
	;;
    esac
echo -n "$contents" > /tmp/orca-ratechanger
echo "Now changing $contents."
exit 0
