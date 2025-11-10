"""Test version information."""

import sys
import pynapcat


def test_python_version():
    """Test that Python version is 3.14+."""
    assert sys.version_info >= (3, 14), "PyNapCat requires Python 3.14+"


def test_version():
    """Test that version is defined."""
    assert hasattr(pynapcat, "__version__")
    assert isinstance(pynapcat.__version__, str)
    assert pynapcat.__version__ == "0.1.0"


def test_module_attributes():
    """Test that module has expected attributes."""
    assert hasattr(pynapcat, "__author__")
    assert hasattr(pynapcat, "__email__")
