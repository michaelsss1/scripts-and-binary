import sys
import os
import time

filename = sys.argv[1]
ip_list = []
port_list = []
with open(filename, 'r') as f:
	for line in f.readlines():
		ip = line.strip('\n').split(" ")[3]
		if ip not in ip_list:
			ip_list.append(ip)
		else:
			pass

with open(filename, 'r') as f1:
	for line in f1.readlines():
		for ip in ip_list:
			if ip == line.strip('\n').split(" ")[3]:
				port = line.strip('\n').split(" ")[2]
				port_list.append(port)
				port_format.join(",")
				print(f"[+] scanning {ip} with {port_format}")
				#os.system(f'nmap -Pn -n -sV -p {port_format} -T4 -oA {ip}.nmap')
				print(f"[+] scanning {ip} done")
				port_list.clear()
				#time.sleep(3)