"""
Root entrypoint for the CYBERHARI Labs application.
Run this file from the project root: python run.py
"""
import uvicorn
import os
import sys

# Add the project root to the Python path so 'server' package resolves correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server.main:app", host="0.0.0.0", port=port, reload=False)
