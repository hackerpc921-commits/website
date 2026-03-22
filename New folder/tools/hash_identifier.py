import sys
import hashlib
import re

def identify_hash(hash_str):
    hash_str = hash_str.strip()
    length = len(hash_str)
    
    print(f"[*] Analyzing hash: {hash_str}")
    print("-" * 50)
    
    potential_types = []
    
    # Simple length-based identification
    if re.match(r"^[a-fA-F0-9]{32}$", hash_str):
        potential_types.append("MD5 / MD4")
    elif re.match(r"^[a-fA-F0-9]{40}$", hash_str):
        potential_types.append("SHA-1")
    elif re.match(r"^[a-fA-F0-9]{56}$", hash_str):
        potential_types.append("SHA-224")
    elif re.match(r"^[a-fA-F0-9]{64}$", hash_str):
        potential_types.append("SHA-256")
    elif re.match(r"^[a-fA-F0-9]{96}$", hash_str):
        potential_types.append("SHA-384")
    elif re.match(r"^[a-fA-F0-9]{128}$", hash_str):
        potential_types.append("SHA-512")
    elif re.match(r"^\$[a-z0-9]+\$[0-9]+\$[A-Za-z0-9+/.]+", hash_str):
        potential_types.append("Bcrypt / Phpass")
    
    if potential_types:
        print("[+] Possible Hash Types:")
        for t in potential_types:
            print(f"  - {t}")
    else:
        print("[-] Could not identify hash type based on standard patterns.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python hash_identifier.py <hash_string>")
        sys.exit(1)
        
    identify_hash(sys.argv[1])

if __name__ == "__main__":
    main()
