import sys
import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Missing uppercase letter.")
        
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Missing lowercase letter.")
        
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Missing numeric digit.")
        
    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    else:
        feedback.append("Missing special character (@$!%*?&#).")
        
    return strength, feedback

def main():
    if len(sys.argv) < 2:
        print("Usage: python password_strength.py <password>")
        sys.exit(1)
        
    password = sys.argv[1]
    strength, feedback = check_password_strength(password)
    
    print(f"[*] Analyzing password security...")
    print("-" * 50)
    
    levels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
    print(f"[!] Strength Level: {levels[strength-1] if strength > 0 else 'Extremely Weak'} ({strength}/5)")
    
    if feedback:
        print("\n[?] Recommendations:")
        for note in feedback:
            print(f"  - {note}")
    else:
        print("\n[+] Great job! This password meets all security criteria.")

if __name__ == "__main__":
    main()
