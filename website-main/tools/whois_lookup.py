import sys
import random
from datetime import datetime

def simulate_whois(domain):
    print(f"[*] Fetching WHOIS data for: {domain}")
    print("-" * 50)
    
    # Mock WHOIS data
    creation_date = datetime(random.randint(2000, 2015), random.randint(1, 12), random.randint(1, 28))
    expiry_date = datetime(2028, random.randint(1, 12), random.randint(1, 28))
    
    print(f"Domain Name: {domain.upper()}")
    print(f"Registry Domain ID: {random.randint(1000000, 9999999)}_DOMAIN_COM-VRSN")
    print(f"Registrar WHOIS Server: whois.registrar.example")
    print(f"Registrar URL: http://www.registrar.example")
    print(f"Updated Date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"Creation Date: {creation_date.strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"Registry Expiry Date: {expiry_date.strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"Registrar: Example Registrar, Inc.")
    print(f"Registrant Organization: {domain.split('.')[0].capitalize()} Protective Services")
    print(f"Name Server: NS1.{domain.upper()}")
    print(f"Name Server: NS2.{domain.upper()}")
    print(f"DNSSEC: unsigned")
    
    print("\n[+] WHOIS Lookup completed (Simulated).")

def main():
    if len(sys.argv) < 2:
        print("Usage: python whois_lookup.py <domain>")
        sys.exit(1)
        
    simulate_whois(sys.argv[1])

if __name__ == "__main__":
    main()
