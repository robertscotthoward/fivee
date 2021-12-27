# http://pythex.org/
import unittest
import math
import re
import random
from money import Money



class DiceTests(unittest.TestCase):
  def t(self, expected, expression):
    money = Money(expression)
    dollars = money.Dollars()
    actual = str(money)
    self.assertEqual(expected, actual)
    return dollars

  def test_roles(self):
    # It adds them all up
    dollars = Money("gp").Dollars()
    self.assertEqual(100, dollars)
    dollars = self.t("1cp 2sp 3ep 4gp 5pp", "1sp 1cp 1sp 1ep 4gp 5pp 2ep")
    self.assertEqual(5571, dollars)
    dollars = self.t("1sp 2ep 3gp", "1sp 2ep 3gp")
    self.assertEqual(410, dollars)


if __name__ == '__main__':
    unittest.main()
