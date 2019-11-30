"""
Test file for pi montecarlo
"""

import unittest
from pi_montecarlo import compute_pi


class TestPi(unittest.TestCase):
    """
    Tests for pi
    """

    def test_number(self):
        """
        Test the accuracy
        """
        pi_aprox = compute_pi(500)
        self.assertGreater(pi_aprox, 2.5)
        self.assertLess(pi_aprox, 3.5)
