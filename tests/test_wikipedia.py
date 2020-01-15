from unittest.mock import Mock

import click
import pytest

from hypermodern_python import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
