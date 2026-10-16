# test_kernelnocturne.py
"""
Tests for KernelNocturne module.
"""

import unittest
from kernelnocturne import KernelNocturne

class TestKernelNocturne(unittest.TestCase):
    """Test cases for KernelNocturne class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KernelNocturne()
        self.assertIsInstance(instance, KernelNocturne)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KernelNocturne()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
