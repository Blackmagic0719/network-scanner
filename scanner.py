import os
import platform
import threading
import socket

# Banner
print("="*40)
print("   Network Scanner by Nimesh")
print("="*40)
print("Scanning network...\n")

# Store active devices
online_devices = []

# Ping function
def ping(ip):
    param = "-n 1 -w 100" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {param} {ip} > nul"
    
    if os.system(command) == 0:
        print(f"[+] {ip} is ONLINE")
        online_devices.append(ip)
        scan_ports(ip)   # scan ports immediately

# Port scanning
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"    [OPEN] Port {port}")
        
        sock.close()
    except:
        pass

def scan_ports(ip):
    print(f"    Scanning ports for {ip}...")
    common_ports = [21, 22, 80, 443]

    for port in common_ports:
        scan_port(ip, port)

# Base IP (your network)
base_ip = "10.22.55."

threads = []

# Create threads for fast scanning
for i in range(1, 255):
    ip = base_ip + str(i)
    t = threading.Thread(target=ping, args=(ip,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

# Summary
print("\n" + "="*40)
print(f"Scan Complete. Devices found: {len(online_devices)}")
print("="*40)