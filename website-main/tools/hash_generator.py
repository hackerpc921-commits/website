import sys
import hashlib

def generate_hashes(data):
    print(f"[*] Generating cryptographic hashes for: {data}")
    print("-" * 50)
    
    # MD5
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    print(f"[+] MD5:      {md5_hash}")
    
    # SHA1
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    print(f"[+] SHA1:     {sha1_hash}")
    
    # SHA256
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    print(f"[+] SHA256:   {sha256_hash}")
    
    print("-" * 50)
    print("[+] Hashing completed.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python hash_generator.py <string>")
        sys.exit(1)
        
    generate_hashes(sys.argv[1])

if __name__ == "__main__":
    main()
