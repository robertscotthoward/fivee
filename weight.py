# http://pythex.org/
import unittest
from tools import *
import re

class Weight:

  def __init__(self, s):
    """
    @s is weight string; e.g. "20 lbs", "10 ounces", "1.5 kilograms". 
    "lbs" is default.
    """
    self.s = s
    Q, U = Weight.Parse(s)
    self.quantity = Q
    self.units = U

  def Parse(s):
    match = re.search(r"(?P<Q>[0-9]+(\.[0-9]+)?)\s*(?P<U>[A-Za-z]+)?", s)
    if not match:
      raise Exception(f'Invalid weight string. Expected format "NUMBER UNITS". Got "{s}"')
    Q = int(match.group("Q") or "1")
    U = match.group("U") or "lbs"
    return Q, U

  def __str__(self):
    return f"{self.quantity} {self.units}"

  def __repr__(self):
    return f"Weight({self.quantity}, '{self.units}')"

