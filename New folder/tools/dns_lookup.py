import sys
import random

def dns_lookup(domain):
    print(f"[*] Fetching DNS records for: {domain}")
    print("-" * 50)
    
    # Simulated DNS Records
    records = {
        "A": [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"],
        "MX": [f"mail.{domain}", f"backup-mail.{domain}"],
        "TXT": ["v=spf1 include:_spf.example.com ~all", "google-site-verification=aB1c2D3e4F5g6H7i8J9k0L"],
        "NS": [f"ns1.{domain}", f"ns2.{domain}"]
    }
    
    for record_type, values in records.items():
        print(f"[+] {record_type} Records:")
        for val in values:
            print(f"  - {val}")
            
    print("\n[+] DNS Lookup completed (Simulated).")

def main():
    if len(sys.argv) < 2:
        print("Usage: python dns_lookup.py <domain>")
        sys.exit(1)
        
    dns_lookup(sys.argv[1])

if __name__ == "__main__":
    main()
