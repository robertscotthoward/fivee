# http://pythex.org/
import unittest
import math
import re
import random


class Money:
  def __init__(self, amount="0"):
    """
    Represents an amount of money normalized to Gold Pieces.
    An amount can be expressed as one or more space-delimited case-insensitive expressions in the format:
    "NUMBER UNIT" where UNIT default is "GP"; e.g. "1sp 3gp 2pp" to represent
    1 silver piece, 3 gold pieces, and 2 platinum pieces.
    """
    self.types = ['cp', 'sp', 'ep', 'gp', 'pp']
    self.names = ['copper', 'silver', 'electrum', 'gold', 'platinum']
    self.coins = [0, 0, 0, 0, 0]
    self.copper = [1, 10, 50, 100, 1000]
    self.Add(amount)

  def Parse(self, amounts):
    coins = [0, 0, 0, 0, 0]
    for e in amounts.split():
      match = re.search(r"(?P<N>[0-9]+)?(?P<C>cp|sp|ep|gp|pp)?", e.lower())
      if not match:
        raise Exception('Invalid list of coins.')
      N = int(match.group("N") or "1")
      C = match.group("C") or "gp"
      try:
        i = self.types.index(C)
        coins[i] += N
      except ex:
        raise "Invalid coin expression '" + e + "'"
    return coins

  def Add(self, amounts):
    amounts = self.Parse(amounts)
    for i in range(len(self.types)):
      self.coins[i] += amounts[i]

  def Copper(self):
    copper = 0
    for i in range(len(self.types)):
      copper += self.coins[i] * self.copper[i]
    return copper

  def Gold(self):
    return self.Copper() / 100

  def Dollars(self):
    'Just a fun equivalent based on an assumption.'
    return round(self.Gold() * 100,2)


  def __str__(self):
    return ' '.join(f"{self.coins[i]}{self.types[i]}" for i in range(len(self.types)) if self.coins[i])


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
