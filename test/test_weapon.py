import unittest
from tools import *
from fluid import Fluid
from weapon import Weapon

class WeaponTests(unittest.TestCase):
  def test_load(self):
    fluid = Fluid()
    fluid.name = "Club"
    fluid.cost = "1sp"
    fluid.damage = "1d4 bludgeoning"
    fluid.weight = "2 lbs"
    fluid.properties = ['light']

    weapon = Weapon(fluid)
    self.assertEqual(10, weapon.cost.Dollars())

if __name__ == '__main__':
    unittest.main()
