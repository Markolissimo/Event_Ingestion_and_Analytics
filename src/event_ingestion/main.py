from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from typing import List, Optional
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")   
    yield
    logger.info("Shutting down...")

app = FastAPI(
    title="Event Ingestion and Analytics Service",
    description="High-performance service for ingesting and analyzing event data",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}

from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Dict, Any

class EventProperties(BaseModel):
    """Dynamic properties for events"""
    pass

class Event(BaseModel):
    """Event model for request/response"""
    event_id: UUID
    occurred_at: datetime
    user_id: str
    event_type: str
    properties: Dict[str, Any] = Field(default_factory=dict)

@app.post("/events", response_model=List[Event])
async def ingest_events(events: List[Event]):
    """
    Ingest multiple events
    
    - **events**: List of events to ingest
    """
    # TODO: Implement actual event processing
    # For now, just return the received events
    return events

@app.get("/stats/dau")
async def get_daily_active_users(
    start_date: str,
    end_date: str = None
):
    """
    Get daily active users count
    
    - **start_date**: Start date in YYYY-MM-DD format
    - **end_date**: End date in YYYY-MM-DD format (defaults to start_date)
    """
    # TODO: Implement actual DAU calculation
    return {"message": "DAU endpoint - implementation pending"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Event Ingestion and Analytics Service",
        "version": "0.1.0",
        "docs": "/docs"
    }