import unittest
import os
import yaml
from tools import *


class ToolsTests(unittest.TestCase):
  def test_1(self):
    self.assertEqual("Hello There", "Hello" + " There")

if __name__ == '__main__':
  unittest.main()
