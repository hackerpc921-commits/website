import sys
import random

def shodan_lookup(ip):
    print(f"[*] Querying Shodan Intelligence for IP: {ip}")
    print("-" * 50)
    
    # Simulated Shodan Data
    data = {
        "OS": random.choice(["Linux 4.x", "Windows Server 2019", "Embedded (IoT)", "Ubuntu 22.04 LTS"]),
        "Ports": sorted(random.sample([80, 443, 22, 21, 3389, 8080, 8443, 53], random.randint(2, 5))),
        "Organization": random.choice(["Amazon.com", "Google Cloud", "Microsoft Corporation", "DigitalOcean", "Private Network"]),
        "Hostnames": [f"ec2-{random.randint(10, 99)}-{random.randint(100, 255)}.compute-1.amazonaws.com"],
        "Vulnerabilities": [f"CVE-2023-{random.randint(1000, 9999)}" if random.random() < 0.3 else "None Detected"]
    }
    
    print(f"Organization: {data['Organization']}")
    print(f"Operating System: {data['OS']}")
    print(f"Hostnames: {', '.join(data['Hostnames'])}")
    print(f"Open Ports: {', '.join(map(str, data['Ports']))}")
    
    print("\n[+] Service Banners:")
    for port in data['Ports']:
        banner = "HTTP/1.1 200 OK\nServer: nginx/1.18.0" if port in [80, 8080] else "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5"
        print(f"  Port {port}: {banner}")
        
    print(f"\n[!] Potential Vulnerabilities: {', '.join(data['Vulnerabilities'])}")
    print("\n[+] Shodan data retrieval completed (Simulated).")

def main():
    if len(sys.argv) < 2:
        print("Usage: python shodan_lookup.py <ip_address>")
        sys.exit(1)
        
    shodan_lookup(sys.argv[1])

if __name__ == "__main__":
    main()
