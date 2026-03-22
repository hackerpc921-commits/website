import sys

def study_guide(topic):
    topic = topic.lower().strip()
    print(f"[*] CYBERHARI Knowledge Base: {topic.upper()}")
    print("-" * 60)
    
    knowledge = {
        "sql injection": {
            "definition": "A vulnerability where an attacker can interfere with the queries that an application makes to its database.",
            "impact": "Data theft, unauthorized access, and complete database compromise.",
            "prevention": "Use parameterized queries (prepared statements) and input validation."
        },
        "phishing": {
            "definition": "A social engineering attack used to steal user data, including login credentials and credit card numbers.",
            "delivery": "Typically via email, SMS (smishing), or voice calls (vishing).",
            "prevention": "Enable MFA, verify sender identity, and avoid clicking suspicious links."
        },
        "xss": {
            "name": "Cross-Site Scripting (XSS)",
            "definition": "A vulnerability that allows an attacker to inject malicious scripts into web pages viewed by other users.",
            "types": "Stored XSS, Reflected XSS, and DOM-based XSS.",
            "prevention": "Sanitize and encode all user-supplied data before rendering it in the browser."
        },
        "encryption": {
            "definition": "The process of encoding information so that only authorized parties can access it.",
            "types": "Symmetric (AES) and Asymmetric (RSA, ECC).",
            "best_practice": "Use modern, well-audited algorithms and keep private keys secure."
        },
        "mfa": {
            "name": "Multi-Factor Authentication",
            "definition": "A security system that requires more than one method of authentication from independent categories.",
            "categories": "Something you know (password), something you have (token), something you are (biometrics).",
            "importance": "Critical defense against credential-based attacks."
        },
        "hacking": {
            "definition": "The act of identifying and exploiting vulnerabilities in computer systems or networks.",
            "categories": "Ethical (White Hat), Malicious (Black Hat), Gray Hat.",
            "phases": "Reconnaissance -> Scanning -> Gaining Access -> Maintaining Access -> Clearing Tracks.",
            "prevention": "Never stop learning, use multi-layered security, and always act ethically."
        },
        "social engineering": {
            "definition": "Manipulating individuals into divesting confidential information or performing actions.",
            "techniques": "Phishing (email), Vishing (voice), Smishing (SMS), Baiting (physical media).",
            "impact": "Account takeover, identity theft, corporate espionage.",
            "prevention": "Security awareness training, verifying identities, the principle of healthy skepticism."
        },
        "ddos": {
            "definition": "Distributed Denial of Service - overwhelming a target with traffic from multiple sources.",
            "types": "Volumetric (UDP/ICMP flood), Protocol (SYN flood), Application Layer (HTTP flood).",
            "impact": "Service downtime, financial loss, reputational damage.",
            "prevention": "Rate limiting, CDN usage, specialized DDoS mitigation scrubbing services."
        },
        "iam": {
            "definition": "Identity and Access Management - ensuring the right individuals have the right access to resources.",
            "concepts": "Identification, Authentication, Authorization, Accounting (AAA).",
            "principles": "Principle of Least Privilege (PoLP), Zero Trust, RBAC (Role-Based Access Control).",
            "best_practices": "Regular access reviews, MFA, strong password policies."
        }
    }
    
    if topic in knowledge:
        data = knowledge[topic]
        for key, value in data.items():
            print(f"[+] {key.upper()}:")
            print(f"    {value}\n")
    else:
        print(f"[-] Topic '{topic}' not found in the basic guide.")
        print("[*] Available topics: " + ", ".join(knowledge.keys()))
        
    print("-" * 60)
    print("[+] Study session completed. Knowledge is power.")

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "sql injection"
    study_guide(target)

if __name__ == "__main__":
    main()
