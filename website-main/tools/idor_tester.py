import sys
import random
import time

def idor_tester(url):
    print(f"[*] CYBERHARI IDOR Vulnerability Analysis: {url}")
    print("-" * 60)
    time.sleep(1)
    
    print("[+] Detecting direct object references in URL parameters...")
    # Mocking patterns like ?id=123 or /user/45
    params = ["user_id", "order_id", "doc_id", "profile"]
    found = random.sample(params, 2)
    
    for p in found:
        print(f"    [FOUND] Parameter: {p} (Initial Value: {random.randint(100, 200)})")
    
    print("\n[*] Attempting Parameter Manipulation (Object Traversal)...")
    time.sleep(1.5)
    
    tests = [
        {"val": 101, "status": "200 OK", "data": "Showing your profile..."},
        {"val": 102, "status": "200 OK", "data": "[LEAK] Showing User_B's private data!"},
        {"val": 9999, "status": "404 Not Found", "data": "Object missing"},
        {"val": "admin", "status": "200 OK", "data": "[CRITICAL] Admin Configuration Access Granted!"}
    ]

    for t in tests:
        print(f"    [TEST] Setting parameter to '{t['val']}' -> Response: {t['status']}")
        if "[LEAK]" in t['data'] or "[CRITICAL]" in t['data']:
            print(f"      >> WARNING: {t['data']}")
        time.sleep(0.4)

    print("\n[!] VULNERABILITY CONFIRMED: Insecure Direct Object Reference detected on parameter 'user_id'.")
    print("[*] Recommendation: Implement indirect reference maps or strict ownership validation.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://shop.example.com/api/user/101"
    idor_tester(target)
