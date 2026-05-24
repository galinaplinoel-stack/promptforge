"""Category definitions and metadata for PromptForge."""


class Category:
    """Represents a single creative category."""

    def __init__(
        self,
        name: str,
        display_name: str,
        icon: str,
        description: str,
        tags: list[str],
    ):
        self.name = name
        self.display_name = display_name
        self.icon = icon
        self.description = description
        self.tags = tags

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "display_name": self.display_name,
            "icon": self.icon,
            "description": self.description,
            "tags": self.tags,
        }


class CategoryManager:
    """Manages all available creative categories."""

    CATEGORIES = {
        "art": Category(
            name="art",
            display_name="Art & Image",
            icon="🎨",
            description="Generate prompts for AI image generators",
            tags=["midjourney", "dalle", "stable-diffusion", "digital-art"],
        ),
        "writing": Category(
            name="writing",
            display_name="Creative Writing",
            icon="✍️",
            description="Story starters, character concepts, world-building",
            tags=["fiction", "novel", "screenplay", "poetry"],
        ),
        "music": Category(
            name="music",
            display_name="Music & Audio",
            icon="🎵",
            description="Prompts for AI music and audio generation",
            tags=["composition", "ambient", "electronic", "orchestral"],
        ),
        "video": Category(
            name="video",
            display_name="Video & Animation",
            icon="🎬",
            description="Storyboard and motion design prompts",
            tags=["cinematic", "animation", "motion-graphics"],
        ),
        "brainstorm": Category(
            name="brainstorm",
            display_name="Brainstorm",
            icon="🧠",
            description="AI-powered idea generation and exploration",
            tags=["ideas", "innovation", "creativity", "problem-solving"],
        ),
        "design": Category(
            name="design",
            display_name="Design System",
            icon="📐",
            description="UI/UX briefs, palettes, and layout concepts",
            tags=["ui", "ux", "typography", "color-palette"],
        ),
    }

    def get(self, name: str) -> Category:
        """Get a category by name."""
        if name not in self.CATEGORIES:
            raise KeyError(f"Unknown category: {name}")
        return self.CATEGORIES[name]

    def is_valid(self, name: str) -> bool:
        """Check if a category name is valid."""
        return name in self.CATEGORIES

    def list_names(self) -> list[str]:
        """List all category names."""
        return list(self.CATEGORIES.keys())

    def list_all(self) -> list[dict]:
        """List all categories with metadata."""
        return [c.to_dict() for c in self.CATEGORIES.values()]

    def search_by_tag(self, tag: str) -> list[Category]:
        """Find categories that have a specific tag."""
        return [c for c in self.CATEGORIES.values() if tag in c.tags]
