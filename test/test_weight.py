import unittest
from tools import *
from weight import Weight

class WeightTests(unittest.TestCase):
  def test_parse(self):
    w = Weight("10")
    print(w)
    self.assertEqual("10 lbs", str(w))
    self.assertEqual("Weight(10, 'lbs')", repr(w))

if __name__ == '__main__':
    unittest.main()
