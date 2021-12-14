# http://pythex.org/
import unittest


class Weapon:
  def __init__(self, obj):
    """
    @obj is the yaml object that represents this class.
    """
    self.obj = obj
    self.name = obj['name']
    self.cost = Cost()

  def Role(self):
    n = 0
    for i in range(self.N):
      n += random.randint(1, self.D)
    if self.SIGN == "+":
        n += self.A
    else:
        n -= self.A
    return n



class WeaponTests(unittest.TestCase):
  def test_1(self):
    pass

if __name__ == '__main__':
    unittest.main()
