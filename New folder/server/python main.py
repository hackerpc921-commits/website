from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .tool_runner import run_cyber_tool
from .database import engine, get_db, SessionLocal
from . import models
from sqlalchemy.orm import Session
from typing import List

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cybersecurity Learning API")

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ToolRequest(BaseModel):
    tool: str
    target: str

class ContactRequest(BaseModel):
    name: str
    email: str
    message: str

@app.get("/")
async def root():
    return {"message": "Cybersecurity Learning Platform API is online."}

@app.post("/contact")
async def contact_hq(request: ContactRequest):
    # In a real app, this would send an email or save to a DB
    print(f"[CONTACT_HQ] New message from {request.name} ({request.email}): {request.message[:50]}...")
    return {"status": "SUCCESS", "message": "Transmission received and decrypted by CYBERHARI Command."}

@app.post("/run-tool")
async def run_tool(request: ToolRequest, db: Session = Depends(get_db)):
    allowed_tools = [
        "port_scanner", "subdomain_finder", "password_strength", 
        "header_analyzer", "whois_lookup", "hash_identifier", 
        "dns_lookup", "ip_geolocation", "base64_converter",
        "shodan_lookup", "packet_sniffer", "vulnerability_scanner",
        "study_guide", "brute_force_simulator", "hash_generator",
        "user_agent_analyzer", "ssl_checker", "firewall_simulator",
        "malware_sandbox", "metadata_extractor", "honeypot_simulator",
        "idor_tester", "csrf_analyzer", "waf_bypass_tester"
    ]
    
    if request.tool not in allowed_tools:
        raise HTTPException(status_code=400, detail="Invalid tool specified.")
    
    output = run_cyber_tool(request.tool, request.target)
    
    # Save to database
    db_result = models.LabHistory(
        tool=request.tool,
        target=request.target,
        output=output
    )
    db.add(db_result)
    db.commit()
    
    return {"output": output}

@app.get("/lab-history")
async def get_history(db: Session = Depends(get_db)):
    history = db.query(models.LabHistory).order_by(models.LabHistory.timestamp.desc()).limit(10).all()
    return history

@app.get("/modules")
async def get_modules():
    return [
        {
            "id": "module-1",
            "title": "Network Reconnaissance",
            "description": "Learn how to discover open ports and services on a target system.",
            "tools": ["port_scanner"]
        },
        {
            "id": "module-2",
            "title": "Subdomain Enumeration",
            "description": "Discover subdomains to expand your attack surface analysis.",
            "tools": ["subdomain_finder"]
        },
        {
            "id": "module-3",
            "title": "Password Security",
            "description": "Analyze password strength and learn about secure authentication.",
            "tools": ["password_strength"]
        },
        {
            "id": "module-4",
            "title": "Web Header Analysis",
            "description": "Inspect HTTP security headers to identify common web vulnerabilities.",
            "tools": ["header_analyzer"]
        },
        {
            "id": "module-5",
            "title": "WHOIS Information",
            "description": "Gather registration data for domains to identify ownership and registration details.",
            "tools": ["whois_lookup"]
        },
        {
            "id": "module-6",
            "title": "Hash Identification",
            "description": "Identify the potential algorithm used to generate a given cryptographic hash.",
            "tools": ["hash_identifier"]
        },
        {
            "id": "module-7",
            "title": "DNS Reconnaissance",
            "description": "Gather DNS records for a domain to understand its infrastructure.",
            "tools": ["dns_lookup"]
        },
        {
            "id": "module-8",
            "title": "IP Intelligence",
            "description": "Geolocate an IP address and identify the hosting organization.",
            "tools": ["ip_geolocation"]
        },
        {
            "id": "module-9",
            "title": "Encoding & Obfuscation",
            "description": "Learn about Base64 encoding and decoding common in many cyber contexts.",
            "tools": ["base64_converter"]
        },
        {
            "id": "module-10",
            "title": "OSINT & Shodan",
            "description": "Use Shodan to gather deep infrastructure intelligence and service banners.",
            "tools": ["shodan_lookup"]
        },
        {
            "id": "module-11",
            "title": "Packet Analysis",
            "description": "Simulate network packet capturing and analyze traffic flow protocols.",
            "tools": ["packet_sniffer"]
        },
        {
            "id": "module-12",
            "title": "Vulnerability Assessment",
            "description": "Perform simplified vulnerability scans to identify known CVEs and misconfigurations.",
            "tools": ["vulnerability_scanner"]
        },
        {
            "id": "module-13",
            "title": "Educational Guide",
            "description": "Access the CYBERHARI knowledge base to learn about key security concepts.",
            "tools": ["study_guide"]
        },
        {
            "id": "module-14",
            "title": "Cracking & Brute Force",
            "description": "Simulate credential attacks and learn about the importance of password complexity.",
            "tools": ["brute_force_simulator"]
        },
        {
            "id": "module-15",
            "title": "Cryptography Utilities",
            "description": "Generate cryptographic hashes (MD5, SHA1, SHA256) for any data string.",
            "tools": ["hash_generator"]
        },
        {
            "id": "module-16",
            "title": "Web Metadata Analysis",
            "description": "Analyze User-Agent strings to identify client operating systems and browsers.",
            "tools": ["user_agent_analyzer"]
        },
        {
            "id": "module-17",
            "title": "Secure Communications",
            "description": "Examine SSL/TLS certificates and verify the security of encrypted connections.",
            "tools": ["ssl_checker"]
        },
        {
            "id": "module-18",
            "title": "Network Protection",
            "description": "Simulate firewall rules and traffic filtering to understand perimeter defense.",
            "tools": ["firewall_simulator"]
        },
        {
            "id": "module-19",
            "title": "Malware Analysis",
            "description": "Perform basic behavioral analysis of suspicious file hashes in a simulated sandbox.",
            "tools": ["malware_sandbox"]
        },
        {
            "id": "module-20",
            "title": "Forensic Intelligence",
            "description": "Extract hidden metadata from documents and images to identify authorship and location.",
            "tools": ["metadata_extractor"]
        },
        {
            "id": "module-21",
            "title": "Defense Engineering",
            "description": "Deploy and monitor fake services to detect and analyze attacker behavior.",
            "tools": ["honeypot_simulator"]
        },
        {
            "id": "module-22",
            "title": "Authorization Testing",
            "description": "Identify Insecure Direct Object Reference (IDOR) vulnerabilities in object-based APIs.",
            "tools": ["idor_tester"]
        },
        {
            "id": "module-23",
            "title": "State-Change Privacy",
            "description": "Analyze cross-site request forgery vulnerabilities and missing anti-CSRF defenses.",
            "tools": ["csrf_analyzer"]
        },
        {
            "id": "module-24",
            "title": "WAF Evasion",
            "description": "Test various obfuscation and double-encoding techniques to bypass web application firewalls.",
            "tools": ["waf_bypass_tester"]
        }
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
