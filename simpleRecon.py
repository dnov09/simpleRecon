#!/bin/python3
import socket
import sys
import pyfiglet as fig
import random

'''
This assignment requires you to write a simple open port scanner using both bash scripting (5 pts) and python scripting (5 pts). The scripts should follow these guidelines

1. Each scipt should take in user input for the ip address to scan (this case scanme.nmap.org)

2. Each script should scan for open ports from  (1 to 1023 ) the well-known ports
'''


def banner():
    font_arr = ["larry3d", "acrobatic", "pyramid", "isometric3", "avatar", "barbwire", "lean", "smkeyboard", "lockergnome"]
    rand = random.randint(1, 3901) % len(font_arr)
    print(fig.figlet_format("s1mpleRec0n", font=font_arr[rand]))


banner()
print("============================================================")
target_input = input("Enter target IP to scan: ")
target_host = socket.gethostbyname(target_input)

try:
    print("============================================================")
    print("Performing port scan on {}".format(target_input))
    print("============================================================")
    print("Port\tService\tStatus")
    


    for ports in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_host, ports))
        if result == 0:
            service = socket.getservbyport(ports)
            print("{}\t{}\tOpen".format(ports, service))

        sock.close()
    
    print("============================================================")
    print("Scan complete")
    print("============================================================")

except socket.gaierror:
    sys.exit()

except socket.error:
    sys.exit()

except KeyboardInterrupt:
    sys.exit()
