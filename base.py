# http://pythex.org/
import unittest
import math
import re
import random


class Base:
  """
  Represents a class that is driven by a YAML branch; i.e. a Fluid object
  """
  def __init__(self, fluid):
    self.fluid = fluid


