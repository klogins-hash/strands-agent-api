# Strands Agent API

FastAPI service for running Strands agents with tools.

## Features

- 🤖 AI agent powered by Strands
- 🧮 Calculator tool for math operations
- ⏰ Current time/date tool
- 📱 SMS sending capability (Twilio integration ready)
- 🔄 Session management for conversation continuity
- 🚀 Production-ready with health checks

## API Endpoints

### `GET /`
Health check endpoint

### `GET /health`
Detailed health status

### `POST /chat`
Main chat endpoint with session support

**Request:**
```json
{
  "message": "What time is it?",
  "session_id": "user123"
}
```

**Response:**
```json
{
  "response": "The current time is...",
  "session_id": "user123"
}
```

### `POST /chat/simple?message=Hello`
Simple chat endpoint using query parameter

### `GET /tools`
List available tools

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `PORT` - Port to run on (default: 8000)

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY="your-key-here"

# Run the server
python main.py
```

Visit http://localhost:8000/docs for interactive API documentation.

## Deploy to Railway

```bash
# Initialize git repo
git init
git add .
git commit -m "Initial commit"

# Deploy to Railway
railway init
railway up
```

Set the `OPENAI_API_KEY` environment variable in Railway dashboard.

## Usage from n8n

Use the HTTP Request node in n8n:

**Method:** POST  
**URL:** `https://your-railway-url.up.railway.app/chat`  
**Body:**
```json
{
  "message": "{{ $json.chatInput }}",
  "session_id": "{{ $json.sessionId }}"
}
```

## Example Requests

### Calculate something
```bash
curl -X POST "https://your-url.up.railway.app/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is 1234 * 5678?"}'
```

### Get current time
```bash
curl -X POST "https://your-url.up.railway.app/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What time is it?"}'
```

### Send SMS
```bash
curl -X POST "https://your-url.up.railway.app/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Send a text to +1234567890 saying hello"}'
```
