# Network Scanner
import scapy.all as scapy
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', dest='target', help='IP RANGE OF TARGET')
    (val) =  parser.parse_args()
    if not val.target:
        parser.error('INVALID ARGS, USE --help')
    return val

def scan(ip):
    arpreq = scapy.ARP(pdst=ip)
    bcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arpreqbcast = bcast/arpreq
    anslst = scapy.srp(arpreqbcast, timeout=1, verbose=False)[0]
    
    clilist = []

    for item in anslst:
        clidic = {'IP':item[1].psrc,'MAC':item[1].hwsrc}
        clilist.append(clidic)
    return clilist

def printres(reslist):
    print('IP ADDRESS\t\t\tMAC ADDRESS\n====================================================')
    for cli in reslist: #add OS/HOST l8r
        print(cli['IP'] + '\t\t' + cli['MAC'])

val = args()
scanres = scan(val.target)
printres(scanres)
