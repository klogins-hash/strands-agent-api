"""
Strands Agent FastAPI Service
A production-ready API wrapper for Strands agents with tools
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
from contextlib import asynccontextmanager

# Import Strands
from strands import Agent, tool
from strands.models import OpenAIModel
from strands_tools import calculator, current_time

# Global agent instance
agent_instance = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize agent on startup"""
    global agent_instance
    
    # Get API key from environment
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if not openai_api_key:
        print("⚠️  Warning: OPENAI_API_KEY not set")
    
    # Define custom SMS tool
    @tool
    def send_sms(phone: str, message: str) -> str:
        '''
        Send an SMS message via Twilio.
        
        Args:
            phone (str): Phone number in E.164 format (e.g., +1234567890)
            message (str): Message to send
        
        Returns:
            str: Confirmation message
        '''
        # TODO: Integrate with actual Twilio API
        return f"SMS sent to {phone}: {message}"
    
    # Create agent with tools
    agent_instance = Agent(
        model=OpenAIModel(
            model_id="gpt-4o-mini",
            api_key=openai_api_key
        ),
        tools=[calculator, current_time, send_sms],
        system_prompt="""You are a helpful AI assistant with access to:
        - calculator: Perform mathematical calculations
        - current_time: Get the current date and time
        - send_sms: Send SMS messages
        
        Be friendly, concise, and use tools when appropriate."""
    )
    
    print("✓ Strands agent initialized")
    yield
    print("✓ Shutting down")

# Create FastAPI app
app = FastAPI(
    title="Strands Agent API",
    description="AI agent with tools powered by Strands",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    response: str
    session_id: str

class ToolInfo(BaseModel):
    name: str
    description: str

class HealthResponse(BaseModel):
    status: str
    version: str
    agent_ready: bool

# Routes
@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "agent_ready": agent_instance is not None
    }

@app.get("/health", response_model=HealthResponse)
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "agent_ready": agent_instance is not None
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat with the Strands agent
    
    The agent has access to:
    - Calculator for math operations
    - Current time/date information
    - SMS sending capabilities
    """
    if not agent_instance:
        raise HTTPException(status_code=503, detail="Agent not initialized")
    
    try:
        # Run the agent
        result = agent_instance(
            request.message,
            session_id=request.session_id
        )
        
        return {
            "response": str(result),
            "session_id": request.session_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

@app.get("/tools", response_model=List[ToolInfo])
async def list_tools():
    """List available tools"""
    return [
        {
            "name": "calculator",
            "description": "Perform mathematical calculations and evaluate expressions"
        },
        {
            "name": "current_time",
            "description": "Get the current date and time"
        },
        {
            "name": "send_sms",
            "description": "Send SMS messages via Twilio"
        }
    ]

@app.post("/chat/simple")
async def chat_simple(message: str):
    """
    Simple chat endpoint (query parameter)
    Example: POST /chat/simple?message=Hello
    """
    if not agent_instance:
        raise HTTPException(status_code=503, detail="Agent not initialized")
    
    try:
        result = agent_instance(message)
        return {"response": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
