import socket
import sys
from datetime import datetime

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                return True
            return False
    except Exception:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python port_scanner.py <host>")
        sys.exit(1)
    
    host = sys.argv[1]
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 993, 995, 3306, 3389, 5432, 8080]
    
    print(f"[*] Starting scan on {host} at {datetime.now()}")
    print("-" * 50)
    
    open_ports = []
    for port in common_ports:
        if scan_port(host, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        else:
            # We don't print closed ports to keep output clean, but we could
            pass
            
    if not open_ports:
        print("[-] No open ports found in the common list.")
    else:
        print(f"\n[*] Scan completed. Found {len(open_ports)} open ports.")

if __name__ == "__main__":
    main()
