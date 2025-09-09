"""AI-powered git commit message generator.

A modern Python CLI tool that generates meaningful commit messages
using AI, with support for multiple providers and advanced configuration.
"""

from __future__ import annotations

__version__ = "0.1.0"
__author__ = "Gareth Daine"
__email__ = "your.email@example.com"

# Re-export key components for easier imports
from .core.exceptions import CommitError, GitError, ConfigError, APIError

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "CommitError",
    "GitError",
    "ConfigError",
    "APIError",
]
