#! /bin/bash

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
