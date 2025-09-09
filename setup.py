"""
Setup configuration for the Sprite CLI package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README file
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="sprite-cli",
    version="1.0.0",
    author="Sprite CLI",
    author_email="sprite@example.com",
    description="A lightweight CLI tool for serving static websites locally",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sprite-cli/sprite",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "sprite=sprite.cli:cli",
        ],
    },
    keywords="static website server cli local development",
    project_urls={
        "Bug Reports": "https://github.com/regularguythatcodes/sprite/issues",
        "Source": "https://github.com/regularguythatcodes/sprite",
    },
)