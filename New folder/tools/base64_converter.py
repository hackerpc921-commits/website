import sys
import base64

def process_base64(data):
    print(f"[*] Base64 Processor")
    print("-" * 50)
    print(f"Input: {data}")
    
    # Try decoding first
    try:
        decoded = base64.b64decode(data).decode('utf-8')
        print(f"\n[+] Decoded Result (UTF-8):")
        print(f"  {decoded}")
    except Exception:
        print("\n[-] Input is not a valid Base64 encoded UTF-8 string.")
        
    # Always provide encoding
    encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    print(f"\n[+] Encoded Result (Base64):")
    print(f"  {encoded}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python base64_converter.py <string_to_process>")
        sys.exit(1)
        
    process_base64(sys.argv[1])

if __name__ == "__main__":
    main()
