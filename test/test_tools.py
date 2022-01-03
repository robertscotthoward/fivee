import unittest
import os
import yaml
from tools import *
from fluid import Fluid


class ToolsTests(unittest.TestCase):
  def test_1(self):
    self.assertEqual("Hello There", "Hello" + " There")

  def yamlSchema(self):
    cls = Fluid("""
first:
  type: string
  required: True
last:
  type: string
  required: True
age:
  type: integer
dob:
  type: date
""")

    obj = Fluid("""
first: Fred
last: Flintstone
age: 20
dob: 2000-01-01
""")

    ValidateYaml(obj, cls)

if __name__ == '__main__':
  unittest.main()
