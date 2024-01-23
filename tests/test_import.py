"""Test examplepackage."""

import examplepackage


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(examplepackage.__name__, str)
