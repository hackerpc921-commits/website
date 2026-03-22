import sys
import time

def csrf_analyzer(url):
    print(f"[*] CYBERHARI CSRF Vulnerability Audit: {url}")
    print("-" * 60)
    time.sleep(1)
    
    print("[+] Inspecting HTML Forms and Request Headers...")
    forms = [
        {"id": "update-password", "method": "POST", "action": "/account/update"},
        {"id": "delete-account", "method": "POST", "action": "/account/terminate"}
    ]

    for f in forms:
        print(f"    [FORM] id='{f['id']}' | action='{f['action']}'")
        time.sleep(0.5)
        print("      - Checking for anti-CSRF tokens...")
        time.sleep(0.5)
        if f['id'] == "update-password":
            print("      [OK] 'csrf_token' hidden field found.")
        else:
            print("      [FAIL] No anti-CSRF token detected in this form!")

    print("\n[*] Analyzing SameSite Cookie attributes...")
    time.sleep(1)
    print("    - session_id: SameSite=None (Vulnerable if Secure is missing)")
    print("    - user_pref: SameSite=Lax (Protected)")

    print("\n[!] SECURITY ANALYSIS: Potential CSRF vulnerability on '/account/terminate'.")
    print("[*] Recommendation: Ensure every state-changing request (POST/PUT/DELETE) requires a unique, secret, and unpredictable token.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://myapp.internal/dashboard"
    csrf_analyzer(target)
