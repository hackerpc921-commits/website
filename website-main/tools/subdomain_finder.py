import sys
import random

def search_subdomains(domain):
    # Mock data for demonstration purposes
    # In a real tool, we might use a wordlist and DNS lookups
    mock_subdomains = ["www", "mail", "dev", "api", "staging", "test", "v1", "v2", "blog", "shop", "support"]
    found = []
    
    print(f"[*] Enumerating subdomains for {domain}")
    print("-" * 50)
    
    # Simulate scanning
    for sub in mock_subdomains:
        # 30% chance to "find" a subdomain
        if random.random() < 0.3:
            full_domain = f"{sub}.{domain}"
            print(f"[+] Found: {full_domain}")
            found.append(full_domain)
            
    if not found:
        print("[-] No subdomains found (Simulated).")
    else:
        print(f"\n[*] Enumeration finished. {len(found)} subdomains discovered.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python subdomain_finder.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    search_subdomains(domain)

if __name__ == "__main__":
    main()
