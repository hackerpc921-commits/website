import sys
import random

def geolocate_ip(ip):
    print(f"[*] Geolocating IP address: {ip}")
    print("-" * 50)
    
    # Simulated Geolocation Data
    cities = ["New York", "London", "Tokyo", "Berlin", "Paris", "Singapore", "Sydney", "Toronto"]
    countries = ["USA", "UK", "Japan", "Germany", "France", "Singapore", "Australia", "Canada"]
    isps = ["DigitalOcean", "Amazon Data Services", "Google LLC", "Cloudflare, Inc.", "Microsoft Corporation"]
    
    idx = random.randint(0, len(cities) - 1)
    
    print(f"IP Address: {ip}")
    print(f"Country: {countries[idx]}")
    print(f"City: {cities[idx]}")
    print(f"Latitude: {random.uniform(-90, 90):.4f}")
    print(f"Longitude: {random.uniform(-180, 180):.4f}")
    print(f"ISP: {random.choice(isps)}")
    print(f"Organization: {random.choice(isps)} LLC")
    print(f"Proxy detected: {'Yes' if random.random() < 0.2 else 'No'}")
    
    print("\n[+] Geolocation data retrieved successfully (Simulated).")

def main():
    if len(sys.argv) < 2:
        print("Usage: python ip_geolocation.py <ip_address>")
        sys.exit(1)
        
    geolocate_ip(sys.argv[1])

if __name__ == "__main__":
    main()
