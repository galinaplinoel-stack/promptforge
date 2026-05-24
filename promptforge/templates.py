"""Prompt templates for each creative category.

Each template is a callable that takes an idea string
and returns a formatted prompt.
"""

from typing import Callable


class TemplateLibrary:
    """Library of prompt templates organized by category."""

    def __init__(self):
        self._templates: dict[str, Callable[[str], str]] = {
            "art": self._art_template,
            "writing": self._writing_template,
            "music": self._music_template,
            "video": self._video_template,
            "brainstorm": self._brainstorm_template,
            "design": self._design_template,
        }

    def get(self, category: str) -> Callable[[str], str]:
        """Get template function for a category."""
        if category not in self._templates:
            raise KeyError(f"No template for category '{category}'")
        return self._templates[category]

    def list_categories(self) -> list[str]:
        """List all available template categories."""
        return list(self._templates.keys())

    @staticmethod
    def _art_template(idea: str) -> str:
        return (
            f"{idea}, ultra-detailed, professional digital art, "
            f"trending on ArtStation, 8K resolution, cinematic lighting, "
            f"volumetric atmosphere, dramatic composition, rich color palette, "
            f"masterpiece quality, sharp focus, intricate details, "
            f"photorealistic rendering"
        )

    @staticmethod
    def _writing_template(idea: str) -> str:
        return (
            f"Write a compelling narrative about: {idea}. "
            f"Use vivid sensory details, complex character development, "
            f"unexpected plot twists, and emotional depth. "
            f"Employ show-don't-tell technique with rich metaphors "
            f"and meaningful subtext throughout."
        )

    @staticmethod
    def _music_template(idea: str) -> str:
        return (
            f"Create a {idea} composition with layered instrumentation, "
            f"dynamic range, emotional progression from contemplative to "
            f"euphoric, organic textures mixed with electronic elements, "
            f"spatial audio design, and cinematic depth."
        )

    @staticmethod
    def _video_template(idea: str) -> str:
        return (
            f"{idea}, cinematic 4K footage, anamorphic lens flare, "
            f"smooth camera movement, professional color grading, "
            f"atmospheric fog, golden hour lighting, film grain texture, "
            f"directed with precision and artistic vision"
        )

    @staticmethod
    def _brainstorm_template(idea: str) -> str:
        return (
            f"Innovative concept: {idea}. Consider the intersection of "
            f"technology and human needs. What problem does this solve? "
            f"Who is the target audience? What makes this 10x better than "
            f"existing solutions? Think about sustainability, accessibility, "
            f"and viral potential."
        )

    @staticmethod
    def _design_template(idea: str) -> str:
        return (
            f"Design concept: {idea}. Create a cohesive visual system with "
            f"harmonious color palette, modern typography, balanced layout, "
            f"clear visual hierarchy, consistent spacing, and accessible "
            f"contrast ratios. Material Design or Neomorphism style."
        )
