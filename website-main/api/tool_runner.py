import subprocess
import os

TOOLS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tools")

def run_cyber_tool(tool_name, target):
    tool_path = os.path.join(TOOLS_DIR, f"{tool_name}.py")
    
    if not os.path.exists(tool_path):
        return f"Error: Tool {tool_name} not found."
    
    try:
        # Run the tool and capture output
        result = subprocess.run(
            ["python", tool_path, target],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout if result.stdout else result.stderr
    except subprocess.TimeoutExpired:
        return "Error: Tool execution timed out."
    except Exception as e:
        return f"Error executing tool: {str(e)}"
