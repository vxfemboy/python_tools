#Mac Address Changer
import subprocess
import optparse
import re

def args():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface','--iface', dest='iface', help='Interface to Change the MAC')
    parser.add_option('-m','--mac', dest='mac', help='Desired Mac Address')
    (val, args) =  parser.parse_args()
    if not val.iface or not val.mac:
        parser.error('INVALID ARGS, USE --help')
    return val

def macchanger(iface,mac):
    print(f'CHANGING IFACE {val.iface} MAC TO {val.mac}')
    subprocess.call(['ifconfig',iface,'down'])
    subprocess.call(['ifconfig',iface,'hw','ether',mac])
    subprocess.call(['ifconfig',iface,'up'])
    

def validmac(iface):
    iface_result = subprocess.check_output(['ifconfig', val.iface])
    macsearch = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', iface_result.decode('utf-8'))
    if macsearch:
        return macsearch.group(0)
    else:
        print('MAC CHANGE FAILED!')

val = args()
cmac = validmac(val.iface)
print(f"CURRENT MAC: {cmac}")
macchanger(val.iface, val.mac)
cmac = validmac(val.iface)

if cmac == val.mac:
    print('MAC CHANGED SUCCESFULLY!')
    print(f'YOUR NEW MAC IS: {val.mac}')
else:
    print('MAC CHANGE FAILED!')