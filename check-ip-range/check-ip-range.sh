#!/bin/bash

# IPs
## find available render machines at subnet
subnet="192.168.56"
## expected range of host machines
hosts=$(seq 11 13)

# declare an empty array of reachble IPs
declare -a reachable=()

for host in $hosts; do
	ip="${subnet}.${host}"
	# count 1, wait 2
	if ping -c 1 -W 2 "$ip" > /dev/null; then
		echo "[OK] Host $ip is reachable."
		# add to array
		reachable+=("$ip")
	else
		echo "[  ] Host $ip is unreachable!"
	fi
done

# print all reachable IPs from array
echo "List of reachable IPs: ${reachable[@]}"
