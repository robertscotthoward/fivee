# http://pythex.org/
import unittest
import re
from dice import Dice
from tools import *


class Damage:
  typestr = "acid,bludgeoning,cold,fire,force,lightning,necrotic,piercing,poison,psychic,radiant,slashing,thunder"
  types = typestr.split(',')

  def __init__(self, s):
    """
    @s is the damage string; e.g. "1d4 bludgeoning"
    """
    self.s = s
    self.dice = Dice(s)
    self.type = s.split()[-1]
    if not self.type in Damage.types:
      raise f"Unrecognized damage type '{self.type}'. Expected [{Damage.typestr}]"

    

