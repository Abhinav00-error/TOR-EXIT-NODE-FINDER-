import requests
import sys
import socket
import json

def display_banner():
    banner = """

      █████████╗ ██████╗ ███████╗     
      ╚══██╔══╝██╔═══██╗██╔════╝     
         ██║   ██║   ██║███████╗     
         ██║   ██║   ██║╚════██║     
         ██║   ╚██████╔╝███████║     
         ╚═╝    ╚═════╝ ╚══════╝     

    \033[91m TOR EXIT NODE FINDER \033[0m
    \033[91m Created by Abhinav VK \033[0m
    \033[92m I AM NOT RESPONSIBLE FOR ANY ILLEGAL USAGE OF THIS TOOL \033[0m
    """
    print(banner)

def get_tor_exit_nodes():
    try:
        response = requests.get("https://check.torproject.org/exit-addresses")
        if response.status_code == 200:
            return response.text
        else:
            print("[!] Failed to retrieve Tor exit node list.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching Tor exit nodes: {e}")
        return None

def is_tor_exit_node(ip, tor_list):
    return ip in tor_list

def get_ip_details(ip):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # Added User-Agent to avoid blocking
        response = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"[!] Error retrieving IP details: {e}")
        return None

def main():
    display_banner()
    if len(sys.argv) != 2:
        print("Usage: python tor_exit_node_finder.py <IP>")
        sys.exit(1)
    
    ip_to_check = sys.argv[1]
    print(f"[*] Checking if {ip_to_check} is a Tor exit node...")
    
    tor_data = get_tor_exit_nodes()
    if not tor_data:
        sys.exit(1)
    
    tor_exit_nodes = set()
    for line in tor_data.split('\n'):
        if line.startswith("ExitAddress"):
            tor_exit_nodes.add(line.split()[1])
    
    if is_tor_exit_node(ip_to_check, tor_exit_nodes):
        print(f"[!] ALERT: {ip_to_check} is a Tor exit node!")
    else:
        print(f"[*] {ip_to_check} is NOT a Tor exit node.")
    
    print("\n[*] Fetching IP details...")
    ip_info = get_ip_details(ip_to_check)
    if ip_info:
        print(json.dumps(ip_info, indent=4))
    else:
        print("[!] Could not retrieve IP details.")

if __name__ == "__main__":
    main()
