from server.tool_runner import run_cyber_tool

def test_tool(name, target):
    print(f"\n--- Testing Tool: {name} on {target} ---")
    output = run_cyber_tool(name, target)
    print(output)
    if "Error" in output:
        print(f"FAILED: {name}")
    else:
        print(f"PASSED: {name}")

if __name__ == "__main__":
    test_tool("port_scanner", "127.0.0.1")
    test_tool("subdomain_finder", "google.com")
    test_tool("password_strength", "StrongP@ss123!")
