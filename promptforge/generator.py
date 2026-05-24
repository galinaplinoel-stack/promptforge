"""Main prompt generation engine.

Handles the core logic of generating enhanced prompts based on
user ideas, categories, and style preferences.
"""

import random
from typing import Optional
from .templates import TemplateLibrary
from .categories import CategoryManager
from .enhancer import PromptEnhancer


class PromptGenerator:
    """AI-powered prompt generator for creative projects."""

    def __init__(self, style: str = "detailed", temperature: float = 0.8):
        self.style = style
        self.temperature = temperature
        self.templates = TemplateLibrary()
        self.categories = CategoryManager()
        self.enhancer = PromptEnhancer()
        self._history: list[dict] = []

    def generate(
        self,
        idea: str,
        category: str = "art",
        style: Optional[str] = None,
        enhance: bool = True,
    ) -> str:
        """Generate a creative prompt from an idea.

        Args:
            idea: The user's creative idea or concept
            category: Target category (art, writing, music, video, brainstorm)
            style: Override default style for this generation
            enhance: Whether to apply AI enhancement to the output

        Returns:
            Generated prompt string
        """
        if not idea or not idea.strip():
            raise ValueError("Idea cannot be empty")

        category = category.lower()
        if not self.categories.is_valid(category):
            raise ValueError(
                f"Invalid category '{category}'. "
                f"Available: {self.categories.list_names()}"
            )

        use_style = style or self.style
        template = self.templates.get(category)
        base_prompt = template.format(idea=idea.strip())

        if enhance:
            base_prompt = self.enhancer.enhance(
                base_prompt,
                category=category,
                style=use_style,
            )

        result = {
            "idea": idea,
            "category": category,
            "style": use_style,
            "prompt": base_prompt,
        }
        self._history.append(result)
        return base_prompt

    def batch_generate(
        self, ideas: list[str], category: str = "art"
    ) -> list[str]:
        """Generate prompts for multiple ideas."""
        return [self.generate(idea, category) for idea in ideas]

    def get_history(self) -> list[dict]:
        """Return generation history."""
        return self._history.copy()

    def clear_history(self):
        """Clear generation history."""
        self._history.clear()

    def random_category(self) -> str:
        """Pick a random category for inspiration."""
        return random.choice(self.categories.list_names())
