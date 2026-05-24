"""PromptForge — AI Creativity Studio

Generate stunning prompts for art, writing, music, video, and brainstorming.
"""

__version__ = "1.0.0"
__author__ = "PromptForge Team"

from .generator import PromptGenerator
from .templates import TemplateLibrary
from .categories import CategoryManager

__all__ = ["PromptGenerator", "TemplateLibrary", "CategoryManager"]
