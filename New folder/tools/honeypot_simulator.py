import sys
import random
import time

def honeypot_simulator(target):
    print(f"[*] CYBERHARI HoneyPot Deployment: {target}")
    print("-" * 60)
    time.sleep(1)
    
    print("[+] Initializing Decoy Services...")
    services = [
        {"port": 21, "name": "FTP (Fake v2.3.4)", "logs": []},
        {"port": 22, "name": "SSH (OpenSSH 7.2p2 - Vulnerable Banner)", "logs": []},
        {"port": 3306, "name": "MySQL (Old Version)", "logs": []}
    ]
    
    for s in services:
        print(f"    [OK] Listening on port {s['port']} -> {s['name']}")
    
    print("\n[*] Monitoring for intrusion attempts...")
    time.sleep(2)
    
    events = [
        {"ip": "192.168.1.45", "action": "Port Scan Detected", "risk": "LOW"},
        {"ip": "185.x.x.x", "action": "Brute Force on SSH (root/password)", "risk": "HIGH"},
        {"ip": "185.x.x.x", "action": "FTP Exploit Attempt (Backdoor)", "risk": "CRITICAL"},
        {"ip": "10.0.x.x", "action": "MySQL Fingerprint Attempt", "risk": "MEDIUM"}
    ]

    for e in events:
        print(f"    [ALERT] {e['ip']} | {e['action']} | Severity: {e['risk']}")
        time.sleep(0.5)

    print("\n[!] INTELLIGENCE GATHERED: Attacker 185.x.x.x is using automated scripts for exploit delivery.")
    print("[*] HoneyPot is successfully diverting traffic and logging telemetry.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "10.0.0.5"
    honeypot_simulator(target)
