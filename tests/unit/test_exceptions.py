"""Test cases for commit exception hierarchy."""

from __future__ import annotations

import pytest

from commit.core.exceptions import (
    CommitError,
    GitError,
    ConfigError,
    APIError,
    ValidationError,
)


class TestCommitError:
    """Test cases for base CommitError class."""

    def test_commit_error_should_inherit_from_exception(self):
        """Test that CommitError inherits from Exception."""
        error = CommitError("test message")
        assert isinstance(error, Exception)

    def test_commit_error_should_store_message(self):
        """Test that CommitError stores the error message."""
        message = "test error message"
        error = CommitError(message)
        assert str(error) == message


class TestGitError:
    """Test cases for GitError class."""

    def test_git_error_should_inherit_from_commit_error(self):
        """Test that GitError inherits from CommitError."""
        error = GitError("git error")
        assert isinstance(error, CommitError)
        assert isinstance(error, Exception)

    def test_git_error_should_store_message(self):
        """Test that GitError stores the error message."""
        message = "git operation failed"
        error = GitError(message)
        assert str(error) == message


class TestConfigError:
    """Test cases for ConfigError class."""

    def test_config_error_should_inherit_from_commit_error(self):
        """Test that ConfigError inherits from CommitError."""
        error = ConfigError("config error")
        assert isinstance(error, CommitError)
        assert isinstance(error, Exception)

    def test_config_error_should_store_message(self):
        """Test that ConfigError stores the error message."""
        message = "configuration invalid"
        error = ConfigError(message)
        assert str(error) == message


class TestAPIError:
    """Test cases for APIError class."""

    def test_api_error_should_inherit_from_commit_error(self):
        """Test that APIError inherits from CommitError."""
        error = APIError("api error")
        assert isinstance(error, CommitError)
        assert isinstance(error, Exception)

    def test_api_error_should_store_message_and_status_code(self):
        """Test that APIError stores message and optional status code."""
        message = "API request failed"
        status_code = 429
        error = APIError(message, status_code)

        assert str(error) == message
        assert error.status_code == status_code

    def test_api_error_should_handle_none_status_code(self):
        """Test that APIError handles None status code."""
        message = "API error without status"
        error = APIError(message)

        assert str(error) == message
        assert error.status_code is None


class TestValidationError:
    """Test cases for ValidationError class."""

    def test_validation_error_should_inherit_from_commit_error(self):
        """Test that ValidationError inherits from CommitError."""
        error = ValidationError("validation error")
        assert isinstance(error, CommitError)
        assert isinstance(error, Exception)

    def test_validation_error_should_store_message(self):
        """Test that ValidationError stores the error message."""
        message = "input validation failed"
        error = ValidationError(message)
        assert str(error) == message
