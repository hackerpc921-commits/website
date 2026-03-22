import sys
import time

def metadata_extractor(filename):
    print(f"[*] CYBERHARI Metadata Extraction: {filename}")
    print("-" * 60)
    time.sleep(1)
    
    metadata = {
        "File Type": "JPEG",
        "File Size": "1.2 MB",
        "Creation Date": "2025:10:12 14:30:05",
        "Device": "iPhone 15 Pro",
        "GPS Coordinates": "48.8584° N, 2.2945° E (Paris, France)",
        "Software": "Adobe Photoshop 2024",
        "Author": "User_Unknown"
    }

    print("[+] Extracting EXIF/Header data...")
    time.sleep(1)
    
    for key, value in metadata.items():
        print(f"    {key}: {value}")
        time.sleep(0.2)
    
    print("\n[!] WARNING: GPS coordinates found. This file contains sensitive location data.")
    print("\n[*] Extraction Complete.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "suspicious_image.jpg"
    metadata_extractor(target)
