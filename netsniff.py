#NETWORK SNIFFER
import scapy.all as scapy # fix issue not reciving
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

def gurl(pacc):
    return pacc[http.HTTPRequest].Host + pacc[http.HTTPRequest].Path

def login(pacc):
    if pacc.haslayer(scapy.Raw):
            load = pacc[scapy.Raw].load #add more fields and threads later
            kywds = ['user', 'pass', 'name', 'mail,', 'word']
            for kywds in b'{kywds}':
                if kywds in load:
                    return load
                    break

def sniffpacc(pacc):
    if pacc.haslayer(http.HTTPRequest): #add https later just http for now 
        url = gurl(pacc)
        print(f'HTTP REQUEST: {url}')
        load = login(pacc)
        if load != 'None':
            print(f'\n\nPOSSIBLE LOGIN FOUND: {load}\n\n') # FIX FOR NO RETURN
        
                

val = args()
sniff(val.iface)
#except OSError: #detect if iface is correct
#    print('INTERFACE NOT FOUND!')
