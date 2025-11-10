"""Test version information."""

import pynapcat


def test_version():
    """Test that version is defined."""
    assert hasattr(pynapcat, "__version__")
    assert isinstance(pynapcat.__version__, str)
    assert pynapcat.__version__ == "0.1.0"


def test_module_attributes():
    """Test that module has expected attributes."""
    assert hasattr(pynapcat, "__author__")
    assert hasattr(pynapcat, "__email__")
