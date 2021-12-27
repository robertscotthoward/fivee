import unittest
import os
import yaml
from tools import *


class Fluid:
  '''
  A Fluid object is one that can model a dict or list, but can be used in a dotted javascript-like manner.
  Example:
    d = {'first': 'Fred', 'last': 'Flintstone'}
  Then you normally need to do this:
    print(d['first'])
  Instead, you can do this:
    fluid = Fluid(d)
    print(fluid.first)  --> which should be easier to read.

  REF: https://rszalski.github.io/magicmethods/
  '''

  def __init__(self, data=None):
    "Called when creating a new object of this class."
    if type(data) is dict:
      self.__dict__["_data"] = data
    elif type(data) is list:
      self.__dict__["_data"] = data
    elif not data:
      self.__dict__["_data"] = None
    else:
      raise Exception(f"Unexpected type '{type(data)}'")

  def __getattr__(self, name):
    "Called when: myObject.SomeName"
    if not self.__dict__["_data"]: return None
    data = self.__dict__["_data"]
    if name in data:
      o = data[name]
      if type(o) is dict or type(o) is list:
        data[name] = Fluid(o)
        return data[name]
      return o
    data[name] = Fluid()
    return data[name]

  def __setattr__(self, name, value):
    "Called when: myObject.SomeName = SomeValue"
    if not self.__dict__["_data"]:
      self.__dict__["_data"] = {}
    data = self.__dict__["_data"]
    if name in data:
      o = data[name]
      if type(o) is dict or type(o) is list:
        return Fluid(o)
    data[name] = value

  def __getitem__(self, key):
    "Called when: myObject[n]. Returns None if n is out of the list range."
    data = self.__dict__["_data"]
    if not data: return None
    #if key < 0: return None
    #if key >= len(data): return None
    o = data[key]
    if type(o) is dict or type(o) is list:
      data[key] = Fluid(o)
      return data[key]
    return o

  def __setitem__(self, key, value):
    "Called when: myObject[n] = SomeValue. Sets the value even if n is out of the list range, and pads to do so."
    if not self.__dict__["_data"]:
      self.__dict__["_data"] = []
    data = self.__dict__["_data"]
    if key < 0: raise Exception("Cannot set negative list indexes.")
    while key >= len(data):
      data.append(None)
    if type(value) is dict or type(value) is list:
      data[key] = Fluid(value)
    data[key] = value

  def normalize(self):
    if not self.__dict__["_data"]:
      return ""
    data = self.__dict__["_data"]
    if type(data) is dict:
      for k in data:
        v = data[k]
        if type(v) is Fluid:
          v.normalize()
          v = v.__dict__["_data"]
          data[k] = v
    elif type(data) is list:
      for i in range(len(data)):
        v = data[i]
        if type(v) is Fluid:
          v.normalize()
          v = v.__dict__["_data"]
          data[i] = v
    return data


  def __nonzero__(self):
    """
    Defines behavior for when bool() is called on an instance of your class. Should return True or False, 
    depending on whether you would want to consider the instance to be True or False.
    """
    if not self.__dict__["_data"]:
      return ""
    data = self.__dict__["_data"]
    if data:
      return True
    return False

  def __add__(self, other):
    if not self.__dict__["_data"]:
      return None
    data = self.__dict__["_data"]
    return data + other


  def __len__(self):
    if self.__dict__["_data"] == None: return 0
    data = self.__dict__["_data"]
    return len(data)

  def __str__(self):
    if self.__dict__["_data"] == None: return ""
    s = yaml.dump(self.normalize())
    return s

  def __repr__(self):
    if self.__dict__["_data"] == None: return ""
    s = yaml.dump(self.normalize())
    return f'''"Fluid("{s}")'''
