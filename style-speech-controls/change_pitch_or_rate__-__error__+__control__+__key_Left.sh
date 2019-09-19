#! /bin/bash

[ -f /tmp/orca-ratechanger ] && contents=$(cat /tmp/orca-ratechanger) || contents="rate"
case "$contents" in
    volume)
	contents="pitch"
	;;
    pitch)
	contents="rate"
	;;
    rate)
	contents="volume"
	;;
    esac
echo -n "$contents" > /tmp/orca-ratechanger
echo "Now changing $contents."
exit 0
