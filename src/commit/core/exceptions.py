"""Exception hierarchy for commit.

This module defines all custom exceptions used throughout the commit
application, providing a clear hierarchy for error handling.
"""

from __future__ import annotations

from typing import Optional


class CommitError(Exception):
    """Base exception for all commit errors.

    This is the root exception class that all other commit-specific
    exceptions inherit from, allowing for broad exception handling.
    """


class GitError(CommitError):
    """Exception raised for git operation related errors.

    This includes errors from git commands, repository state issues,
    and git configuration problems.
    """


class ConfigError(CommitError):
    """Exception raised for configuration related errors.

    This includes invalid configuration files, missing required settings,
    and configuration validation failures.
    """


class APIError(CommitError):
    """Exception raised for AI API related errors.

    This includes network errors, authentication failures, rate limiting,
    and invalid API responses.
    """

    def __init__(self, message: str, status_code: Optional[int] = None) -> None:
        """Initialize APIError with message and optional status code.

        Args:
            message: Error message describing the API failure
            status_code: HTTP status code if applicable
        """
        super().__init__(message)
        self.status_code = status_code


class ValidationError(CommitError):
    """Exception raised for input validation errors.

    This includes invalid user input, malformed data structures,
    and constraint violations.
    """
