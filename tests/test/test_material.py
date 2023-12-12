"""Test Pipe class.

make test T=test_material.py
"""
from . import TestBase


class TestsMaterial(TestBase):
    """PipeMaterial class."""

    def test_material(self):
        """Check as string."""
        assert "smys 20000" in str(self.material)
        assert self.material.smys == 20000
