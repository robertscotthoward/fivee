# http://pythex.org/
import unittest
import re
import random


class Dice:
  def __init__(self, dice = "d100", seed = None):
    """
    @dice is a string in the format "NdD±A"; e.g. "d20", "2d6+3", "10d12-6"
    N is the number of dice to roll (default = 1)
    D is the type of die; can be any sided die; e.g. 33
    A is the optional adjustment to add to the sum of the dice
    """
    self.dice = dice
    # See https://pythex.org/
    match = re.search(r"(?P<N>[0-9]+)?d(?P<D>[0-9]+)((?P<SIGN>[+-])(?P<A>[0-9]+))?", dice)
    if not match:
      raise Exception('Invalid dice string. Expected format "NdD±A"')
    self.N = int(match.group("N") or "1")
    self.D = int(match.group("D") or "100")
    self.A = int(match.group("A") or "0")
    self.SIGN = match.group("SIGN") or "+"
    random.seed(seed)

  def Role(self):
    n = 0
    for i in range(self.N):
      n += random.randint(1, self.D)
    if self.SIGN == "+":
        n += self.A
    else:
        n -= self.A
    return n



class DiceTests(unittest.TestCase):
  def Role10(self, dice, expected):
    dice = Dice(dice, 123)
    a = [str(dice.Role()) for x in range(10)]
    r = ','.join(a)
    if r != expected:
        print(r)
    self.assertEqual(expected, r)

  def test_roles(self):
      self.Role10("2d10", "6,9,7,8,18,12,4,9,15,7")
      self.Role10("1d2", "1,2,1,2,2,1,1,2,2,2")
      self.Role10("2d2", "3,3,3,3,4,2,3,3,2,3")
      self.Role10("3d6+3", "8,11,13,14,8,14,13,9,13,13")
      self.Role10("3d6-3", "2,5,7,8,2,8,7,3,7,7")
      self.Role10("d2-1", "0,1,0,1,1,0,0,1,1,1")


if __name__ == '__main__':
    unittest.main()
