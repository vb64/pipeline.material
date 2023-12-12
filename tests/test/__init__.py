"""Root class for testing."""
from unittest import TestCase


class TestBase(TestCase):
    """Base class for tests."""

    def setUp(self):
        """Set up test data."""
        super(TestBase, self).setUp()
        from pipeline_material import PipeMaterial

        self.material = PipeMaterial("Steel", 20000)
