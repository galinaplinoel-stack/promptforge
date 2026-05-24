"""Prompt enhancement engine.

Adds stylistic modifiers, quality boosters, and category-specific
enhancements to generated prompts.
"""

import random
from typing import Optional


class PromptEnhancer:
    """Enhances prompts with stylistic and quality modifiers."""

    QUALITY_BOOSTERS = [
        "masterpiece", "best quality", "highly detailed",
        "professional", "award-winning", "stunning",
        "photorealistic", "ultra-detailed", "8K resolution",
    ]

    STYLE_MODIFIERS = {
        "detailed": [
            "intricate details", "sharp focus", "high resolution",
            "fine textures", "precise rendering",
        ],
        "artistic": [
            "expressive brushstrokes", "vibrant palette",
            "emotional depth", "artistic composition",
        ],
        "minimal": [
            "clean lines", "negative space", "simple composition",
            "elegant simplicity", "muted tones",
        ],
        "cinematic": [
            "film grain", "anamorphic lens", "dramatic lighting",
            "depth of field", "color grading",
        ],
        "surreal": [
            "dreamlike atmosphere", "impossible geometry",
            "ethereal glow", "otherworldly", "fantastical",
        ],
    }

    CATEGORY_KEYWORDS = {
        "art": ["digital art", "illustration", "concept art"],
        "writing": ["narrative", "prose", "storytelling"],
        "music": ["composition", "arrangement", "production"],
        "video": ["footage", "cinematography", "direction"],
        "brainstorm": ["innovation", "strategy", "ideation"],
        "design": ["layout", "visual system", "interface"],
    }

    def enhance(
        self,
        prompt: str,
        category: str = "art",
        style: str = "detailed",
        intensity: float = 0.7,
    ) -> str:
        """Enhance a prompt with quality boosters and style modifiers.

        Args:
            prompt: Base prompt to enhance
            category: Target category for keyword selection
            style: Style preset to apply
            intensity: How many modifiers to add (0.0-1.0)

        Returns:
            Enhanced prompt string
        """
        intensity = max(0.0, min(1.0, intensity))
        additions = []

        # Add quality boosters
        n_quality = max(1, int(len(self.QUALITY_BOOSTERS) * intensity * 0.3))
        additions.extend(random.sample(self.QUALITY_BOOSTERS, n_quality))

        # Add style modifiers
        if style in self.STYLE_MODIFIERS:
            mods = self.STYLE_MODIFIERS[style]
            n_style = max(1, int(len(mods) * intensity))
            additions.extend(random.sample(mods, n_style))

        # Add category-specific keywords
        if category in self.CATEGORY_KEYWORDS:
            keywords = self.CATEGORY_KEYWORDS[category]
            additions.extend(random.sample(keywords, min(2, len(keywords))))

        if additions:
            return f"{prompt}, {', '.join(additions)}"
        return prompt

    def list_styles(self) -> list[str]:
        """List available style presets."""
        return list(self.STYLE_MODIFIERS.keys())

    def add_style(self, name: str, modifiers: list[str]):
        """Register a custom style preset."""
        self.STYLE_MODIFIERS[name] = modifiers
