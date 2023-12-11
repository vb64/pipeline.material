"""Test Pipe class.

make test T=test_material.py
"""
from . import TestBase


class TestsMaterial(TestBase):
    """PipeMaterial class."""

    def test_material(self):
        """Check as string."""
        assert str(self.material) == 'xxx'
        assert self.material.smys == 20000
