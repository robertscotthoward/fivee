# http://pythex.org/
import unittest
from tools import *
from money import Money


class Weapon:

  def __init__(self, obj):
    """
    @obj is the yaml object that represents this class.
    """
    self.obj = obj
    self.name = obj['name']
    self.properties = obj['properties']
    self.cost = Money(obj["cost"])
    self.damage = Damage(obj["damage"])
    self.weight = Damage(obj["weight"])

    # Validation




class WeaponTests(unittest.TestCase):
  def test_load(self):
    yaml = '''
club:
  name: Club
  cost: 1sp
  damage: 1d4 bludgeoning
  weight: 2 lbs
  properties: light
    '''
    y = ParseYaml(yaml)
    weapon = Weapon(y['club'])
    self.assertEqual(10, weapon.cost.Dollars())
    self.assertEqual(10, weapon.damage)

if __name__ == '__main__':
    unittest.main()
