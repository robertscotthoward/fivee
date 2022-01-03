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
    self.Add(str(amount))

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
