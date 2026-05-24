"""PromptForge REST API server.

Provides HTTP endpoints for prompt generation, category listing,
and template browsing.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

import sys
sys.path.insert(0, "..")
from promptforge import PromptGenerator, __version__

app = FastAPI(
    title="PromptForge API",
    description="AI-powered creativity studio API",
    version=__version__,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = PromptGenerator()


class GenerateRequest(BaseModel):
    """Request body for prompt generation."""
    idea: str = Field(..., min_length=1, description="Creative idea or concept")
    category: str = Field(default="art", description="Target category")
    style: Optional[str] = Field(default=None, description="Style preset")
    enhance: bool = Field(default=True, description="Apply enhancement")


class GenerateResponse(BaseModel):
    """Response body for prompt generation."""
    prompt: str
    category: str
    style: str
    idea: str


@app.get("/")
def root():
    """API health check."""
    return {
        "name": "PromptForge API",
        "version": __version__,
        "status": "running",
    }


@app.post("/generate", response_model=GenerateResponse)
def generate_prompt(req: GenerateRequest):
    """Generate a creative prompt from an idea."""
    try:
        result = generator.generate(
            idea=req.idea,
            category=req.category,
            style=req.style,
            enhance=req.enhance,
        )
        return GenerateResponse(
            prompt=result,
            category=req.category,
            style=req.style or generator.style,
            idea=req.idea,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/categories")
def list_categories():
    """List all available creative categories."""
    return {"categories": generator.categories.list_all()}


@app.get("/styles")
def list_styles():
    """List available style presets."""
    return {"styles": generator.enhancer.list_styles()}


@app.get("/history")
def get_history():
    """Get generation history for this session."""
    return {"history": generator.get_history()}


@app.post("/batch")
def batch_generate(ideas: list[str], category: str = "art"):
    """Generate prompts for multiple ideas at once."""
    try:
        results = generator.batch_generate(ideas, category)
        return {"prompts": results}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
