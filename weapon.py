# http://pythex.org/
import unittest
from tools import *
from money import Money
from damage import Damage
from weight import Weight


class Weapon:

  def __init__(self, fluid):
    """
    @obj is the yaml object that represents this class.
    """
    self.obj = fluid
    self.name = fluid.name
    self.properties = fluid.properties
    self.cost = Money(fluid.cost)
    self.damage = Damage(fluid.damage)
    self.weight = Weight(fluid.weight)

    # Validation

