# http://pythex.org/
import unittest
import math
import fluid
from tools import *


class Data (fluid.Fluid):
  """
  This class wraps the entire data.yaml file. You can substitute your own if needed.
  But this class ensures that the yaml conforms to expectations.
  """

  def __init__(self, data = None):
    """
    @data is the object returned from calling:
      data = ReadYaml("data.yaml")
    """
    if not data:
      data = ReadYaml("data.yaml")
    super().__init__(data)
    
  def GetAbility(self, key):
    """
    @key can be any string that matches an ability's abbr, symbol, or name value.
    EXAMPLE:
    ability = data.GetAbility("str")
    ASSERT: ability == 
    """
    key = key.lower();
    for ability in self.abilities:
      if ability.abbr.lower() == key: return ability
      if ability.symbol.lower() == key: return ability
      if ability.name.lower() == key: return ability
    raise Exception(f"Ability '{key}' not found.")
