#!/bin/bash
# Test the Strands Agent API locally

echo "🚀 Starting Strands Agent API locally..."
echo ""

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  Warning: OPENAI_API_KEY not set"
    echo "Set it with: export OPENAI_API_KEY='your-key-here'"
    echo ""
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt

# Start the server
echo ""
echo "✓ Starting server on http://localhost:8000"
echo "✓ API docs available at http://localhost:8000/docs"
echo ""

python main.py
