#!/usr/bin/env python3
"""
Deploy Strands Agent API to Railway via Web UI
This script opens the Railway dashboard for easy deployment
"""

import webbrowser
import os

def deploy_to_railway():
    """Open Railway dashboard for deployment"""
    
    print("🚂 Deploying Strands Agent API to Railway")
    print("=" * 60)
    print()
    
    # Get current directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("📁 Project directory:", project_dir)
    print()
    print("📋 Deployment Steps:")
    print()
    print("1. Opening Railway dashboard...")
    print("2. Click 'New Project'")
    print("3. Select 'Empty Project'")
    print("4. Click 'Deploy from GitHub repo' or use Railway CLI")
    print()
    print("⚙️  Required Environment Variables:")
    print("   - OPENAI_API_KEY: Your OpenAI API key")
    print()
    print("📚 Files ready for deployment:")
    print("   ✓ main.py - FastAPI application")
    print("   ✓ requirements.txt - Dependencies")
    print("   ✓ Procfile - Start command")
    print("   ✓ railway.json - Railway configuration")
    print()
    
    # Open Railway dashboard
    railway_url = "https://railway.app/new"
    print(f"🌐 Opening: {railway_url}")
    webbrowser.open(railway_url)
    
    print()
    print("=" * 60)
    print("✓ Railway dashboard opened in your browser")
    print()
    print("Alternative: Use Railway CLI")
    print("  $ railway login")
    print("  $ railway init")
    print("  $ railway up")
    print("=" * 60)

if __name__ == "__main__":
    deploy_to_railway()
