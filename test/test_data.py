# http://pythex.org/
import unittest
import re
import random
from data import Data
from dice import Dice


class DataTests(unittest.TestCase):
  def test_abilities(self):
    data = Data()
    self.assertEqual(6, len(data.abilities))
    ability = data.GetAbility("s")
    self.assertEqual("Strength", ability.name)
    ability = data.GetAbility("S")
    self.assertEqual("Strength", ability.name)
    ability = data.GetAbility("STRENGTH")
    self.assertEqual("Strength", ability.name)
    ability = data.GetAbility("Str")
    self.assertEqual("Strength", ability.name)

    ability = data.GetAbility("i")
    self.assertEqual("Intelligence", ability.name)

    ability = data.GetAbility("w")
    self.assertEqual("Wisdom", ability.name)

    ability = data.GetAbility("d")
    self.assertEqual("Dexterity", ability.name)

    ability = data.GetAbility("c")
    self.assertEqual("Constitution", ability.name)

    ability = data.GetAbility("h")
    self.assertEqual("Charisma", ability.name)

    #self.assertRaises(Exception, data.GetAbility, "xyzzy")

if __name__ == '__main__':
    unittest.main()
