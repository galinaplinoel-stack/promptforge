"""Tests for PromptForge generator."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from promptforge import PromptGenerator


def test_generate_art():
    """Test basic art prompt generation."""
    gen = PromptGenerator()
    result = gen.generate("cyberpunk city", category="art")
    assert "cyberpunk city" in result
    assert len(result) > 50


def test_generate_writing():
    """Test writing prompt generation."""
    gen = PromptGenerator()
    result = gen.generate("a detective in space", category="writing")
    assert "detective" in result.lower() or "space" in result.lower()


def test_generate_all_categories():
    """Test generation works for all categories."""
    gen = PromptGenerator()
    for cat in gen.categories.list_names():
        result = gen.generate("test idea", category=cat)
        assert len(result) > 20


def test_invalid_category():
    """Test that invalid category raises error."""
    gen = PromptGenerator()
    try:
        gen.generate("test", category="invalid")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_empty_idea():
    """Test that empty idea raises error."""
    gen = PromptGenerator()
    try:
        gen.generate("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_batch_generate():
    """Test batch generation."""
    gen = PromptGenerator()
    results = gen.batch_generate(["idea1", "idea2", "idea3"], "art")
    assert len(results) == 3


def test_history():
    """Test generation history tracking."""
    gen = PromptGenerator()
    gen.generate("test1", "art")
    gen.generate("test2", "writing")
    assert len(gen.get_history()) == 2
    gen.clear_history()
    assert len(gen.get_history()) == 0


if __name__ == "__main__":
    tests = [
        test_generate_art,
        test_generate_writing,
        test_generate_all_categories,
        test_invalid_category,
        test_empty_idea,
        test_batch_generate,
        test_history,
    ]
    for t in tests:
        try:
            t()
            print(f"  ✅ {t.__name__}")
        except Exception as e:
            print(f"  ❌ {t.__name__}: {e}")
    print("\nAll tests complete!")
