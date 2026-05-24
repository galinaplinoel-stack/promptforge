# PromptForge — AI Creativity Studio

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-purple" alt="version">
  <img src="https://img.shields.io/badge/python-3.10+-blue" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
</p>

> ⚡ AI-powered creativity studio. Generate stunning prompts for art, writing, music, video, and brainstorming.

## ✨ Features

- 🎨 **Art & Image Prompts** — Generate prompts for Midjourney, DALL-E, Stable Diffusion
- ✍️ **Creative Writing** — Story starters, character concepts, world-building
- 🎵 **Music & Audio** — Prompts for AI music generators
- 🎬 **Video & Animation** — Storyboard and motion design prompts
- 🧠 **Brainstorm Engine** — AI-powered idea generation
- 📐 **Design System** — UI/UX briefs and color palette concepts
- 🌐 **Web Interface** — Beautiful dark-themed interactive UI

## 📁 Project Structure

```
promptforge/
├── promptforge/              # Core Python package
│   ├── __init__.py           # Package init + version
│   ├── generator.py          # Main prompt generation engine
│   ├── templates.py          # Prompt templates per category
│   ├── categories.py         # Category definitions & metadata
│   └── enhancer.py           # Prompt enhancement & styling
├── api/                      # REST API server
│   ├── __init__.py
│   └── main.py               # FastAPI application
├── web/                      # Frontend
│   └── index.html            # Interactive web UI
├── tests/                    # Test suite
│   ├── __init__.py
│   └── test_generator.py     # Generator tests
├── config.example.yaml       # Configuration template
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
├── vercel.json               # Vercel deployment config
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Quick Start

### Install
```bash
pip install -r requirements.txt
```

### Run API Server
```bash
cd api
uvicorn main:app --reload --port 8000
```

### Run Web Interface
```bash
cd web
python -m http.server 3000
# Open http://localhost:3000
```

### Use as Python Library
```python
from promptforge import PromptGenerator

gen = PromptGenerator()
prompt = gen.generate(
    idea="A futuristic underwater city",
    category="art",
    style="detailed"
)
print(prompt)
```

## 🔧 Configuration

Copy `config.example.yaml` to `config.yaml` and customize:

```yaml
api:
  host: "0.0.0.0"
  port: 8000
  debug: false

generator:
  default_style: "detailed"
  max_tokens: 500
  temperature: 0.8

categories:
  enabled:
    - art
    - writing
    - music
    - video
    - brainstorm
    - design
```

## 🧪 Testing

```bash
python -m pytest tests/ -v
```

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

Built with ❤️ by the PromptForge team
