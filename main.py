#!/usr/bin/env python3
import subprocess

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] MAC address changed to", new_mac)

def change_ip(interface, new_ip):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "inet",
                    new_ip, "netmask", "255.255.255.0"])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] IP address changed to", new_ip)

def show_banner():
    subprocess.call(["toilet", "-f", "big", "ANONYMXUS"])
    print("\nBY:FRANKOSAV\n")

show_banner()

print("[1]+ Change MAC address and IP address")
print("[2]+ Quit")

choice = input("Enter your choice: ")

if choice == "1":
    interface = input("Enter interface name: ")
    new_mac = input("Enter new MAC address: ")
    new_ip = input("Enter new IP address: ")
    change_mac(interface, new_mac)
    change_ip(interface, new_ip)
elif choice == "2":
    print("Goodbye!")
else:
    print("Error invalid option")
