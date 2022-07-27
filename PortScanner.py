#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, This is Dungy's nmap scanner tool")
print("<------------------------------------------>")

ip_addr = input("Please Enter Ip: ")
print("Ip you entered is: " + ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run 
                1)Light
                2)Medium
                3)Hard
                4)Intense """)
print("You selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())
