import unittest


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        form lgtm.core import lgtm
        self.assertIsNotNone(lgtm('./python.jpeg', 'LGTM'))
