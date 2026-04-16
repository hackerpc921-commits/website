import sys
import random
import time

def firewall_simulator(target):
    print(f"[*] CYBERHARI Firewall Simulation: {target}")
    print("-" * 60)
    time.sleep(1)
    
    rules = [
        {"action": "ALLOW", "port": 80, "protocol": "TCP", "desc": "HTTP Traffic"},
        {"action": "ALLOW", "port": 443, "protocol": "TCP", "desc": "HTTPS Traffic"},
        {"action": "BLOCK", "port": 22, "protocol": "TCP", "desc": "SSH Access (Restricted)"},
        {"action": "BLOCK", "port": 3389, "protocol": "TCP", "desc": "RDP Access (Unauthorized)"},
        {"action": "ALLOW", "port": 53, "protocol": "UDP", "desc": "DNS resolution"}
    ]

    print("[+] Active Firewall Ruleset:")
    for r in rules:
        print(f"    {r['action']} {r['protocol']} port {r['port']} -> {r['desc']}")
    
    print("\n[*] Running Traffic Simulation...")
    time.sleep(1)
    
    packets = [
        {"src": "IP_INTERNAL", "dst": target, "port": 443, "result": "PASSED"},
        {"src": "185.x.x.x", "dst": target, "port": 22, "result": "DROPPED (Rule #3)"},
        {"src": "92.x.x.x", "dst": target, "port": 80, "result": "PASSED"},
        {"src": "IP_EXTERNAL", "dst": target, "port": 3389, "result": "DROPPED (Rule #4)"}
    ]

    for p in packets:
        print(f"    [MOD_FW] Packet from {p['src']} to {p['dst']}:{p['port']} -> {p['result']}")
        time.sleep(0.5)

    print("\n[*] Simulation Complete. Firewall is functioning within parameters.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.1"
    firewall_simulator(target)
