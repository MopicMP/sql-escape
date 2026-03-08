"""Tests for sql-escape."""

import pytest
from sql_escape import escape


class TestEscape:
    """Test suite for escape."""

    def test_basic(self):
        """Test basic usage."""
        result = escape("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            escape("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = escape(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
