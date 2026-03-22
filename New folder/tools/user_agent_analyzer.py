import sys
import re

def analyze_ua(ua):
    print(f"[*] Analyzing User-Agent String")
    print("-" * 50)
    print(f"UA: {ua}")
    print("-" * 50)
    
    # Simple patterns
    os_patterns = {
        "Windows": r"Windows NT ([\d.]+)",
        "Mac OS X": r"Mac OS X ([\d_.]+)",
        "Linux": r"Linux",
        "Android": r"Android ([\d.]+)",
        "iOS": r"iPhone OS ([\d_.]+)|iPad|iPod"
    }
    
    browser_patterns = {
        "Chrome": r"Chrome/([\d.]+)",
        "Firefox": r"Firefox/([\d.]+)",
        "Safari": r"Version/([\d.]+).*Safari",
        "Edge": r"Edg/([\d.]+)",
        "Opera": r"OPR/([\d.]+)"
    }
    
    detected_os = "Unknown"
    for os_name, pattern in os_patterns.items():
        if re.search(pattern, ua):
            detected_os = os_name
            break
            
    detected_browser = "Unknown"
    for browser_name, pattern in browser_patterns.items():
        if re.search(pattern, ua):
            detected_browser = browser_name
            break
            
    print(f"[+] Detected OS:      {detected_os}")
    print(f"[+] Detected Browser: {detected_browser}")
    
    # Mobile detection
    if "Mobile" in ua:
        print(f"[+] Device Category:  Mobile")
    else:
        print(f"[+] Device Category:  Desktop/Tablet")
        
    print("-" * 50)
    print("[+] User-Agent Analysis completed.")

def main():
    if len(sys.argv) < 2:
        # Default fallback
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    else:
        ua = sys.argv[1]
        
    analyze_ua(ua)

if __name__ == "__main__":
    main()
