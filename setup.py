from setuptools import setup, find_packages

setup(
    name="promptforge",
    version="1.0.0",
    description="AI-powered creativity studio — generate prompts for art, writing, music, and more",
    author="PromptForge Team",
    packages=find_packages(exclude=["tests", "api", "web"]),
    python_requires=">=3.10",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: General",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
