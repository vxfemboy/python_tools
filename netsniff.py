#NETWORK SNIFFER
import scapy.all as scapy
import argparse
from scapy.layers import http

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--interface','--iface', dest='iface', help='Interface to Change the MAC')
    (val) =  parser.parse_args() #add filter args l8r
    if not val.iface:
        parser.error('INVALID ARGS, USE --help')
    return val

def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=sniffpacc)

def sniffpacc(pacc):
    if pacc.haslayer(http.HTTPRequest): #add https later 
        print(pacc)

val = args()
sniff(val.iface)
#except OSError: #detect if iface is correct
#    print('INTERFACE NOT FOUND!')
