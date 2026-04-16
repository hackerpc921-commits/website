import sys
import random

def analyze_headers(target):
    print(f"[*] Analyzing security headers for: {target}")
    print("-" * 50)
    
    # Mock headers for demonstration
    headers = {
        "Content-Security-Policy": "default-src 'self'",
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Referrer-Policy": "no-referrer",
        "Server": "Cloudflare",
    }
    
    # Randomly "miss" some headers to provide variety in the lab
    missing = ["X-XSS-Protection", "Permissions-Policy"]
    
    print("[+] Found Headers:")
    for key, val in headers.items():
        print(f"  - {key}: {val}")
        
    print("\n[!] Security Analysis:")
    if "Content-Security-Policy" in headers:
        print("  - CSP Found: Good protection against XSS.")
    
    if "X-Frame-Options" in headers:
        print("  - X-Frame-Options Found: Protected against Clickjacking.")
        
    for m in missing:
        print(f"  - MISSING: {m} (Low Risk)")

    print("\n[+] Analysis complete.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python header_analyzer.py <url_or_host>")
        sys.exit(1)
        
    analyze_headers(sys.argv[1])

if __name__ == "__main__":
    main()
