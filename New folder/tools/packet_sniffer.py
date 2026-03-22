import sys
import random
import time

def simulate_sniffing(interface, count=10):
    print(f"[*] Starting Packet Sniffing on interface: {interface}")
    print(f"[*] Capturing {count} packets...")
    print("-" * 60)
    print(f"{'TIME':<10} {'SRC_IP':<15} {'DST_IP':<15} {'PROTO':<8} {'SIZE':<6}")
    
    protocols = ["TCP", "UDP", "ICMP", "HTTP", "TLSv1.3", "DNS"]
    
    for i in range(count):
        src = f"192.168.1.{random.randint(2, 254)}"
        dst = f"10.0.0.{random.randint(2, 254)}"
        proto = random.choice(protocols)
        size = random.randint(40, 1500)
        timestamp = time.strftime("%H:%M:%S")
        
        print(f"{timestamp:<10} {src:<15} {dst:<15} {proto:<8} {size:<6}")
        # Small delay for realism
        time.sleep(0.1)
        
    print("-" * 60)
    print(f"[+] Capture complete. Total packets: {count}")
    print("[+] Analyzing traffic patterns... No anomalies detected.")

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "eth0"
    simulate_sniffing(target)

if __name__ == "__main__":
    main()
