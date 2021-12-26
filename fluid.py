import unittest
import os
import yaml
from tools import *


class FluidIterator:
  def __init__(self, fluid):
    self.fluid = fluid

  def __iter__(self):
    data = self.fluid.__dict__["_data"]
    return data.__iter__()

  def __next__(self):
    data = self.__dict__["_data"]
    return data.__next__()
    if data:
      if type(data) is list:
        if self._key < len(data):
          current = data[self._key]
          self._key += 1
          return current
      if type(data) is dict:
          current = data.keys()[self._key]
          self._key += 1
          return current
    raise StopIteration


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

def subloadYaml(data):
  '''
  Modify data by loading in any references to external files.
  This is sort of like an "include" statement.
  '''
  # If it's a list, then recur on each item.
  if type(data) == list:
    for x in data:
      subloadYaml(x)

  # If it's a dict then look for a 'ref'.
  elif type(data) == dict:
    # Does it have a 'ref' property?
    if 'ref' in data:
      # Yes, so that means to replace it with the external file.
      data['ref'] = ReadYaml(data['ref'])
    else:
      # No, so recur on each property.
      for k in data:
        subloadYaml(data[k])


def ParseYaml(s):
  '''
  Parses a yaml string into an object.
  If any parts of the file refer to other files, read those in recursively.
  See: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
  '''
  data = yaml.safe_load(s)
  subloadYaml(data)
  return data


def ReadYaml(fn):
  '''
  Read a *.yaml file from the "data" folder into a dict (i.e. dictionary) object.
  If any parts of the file refer to other files, read those in recursively.
  See: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
  '''
  dn = GetDataPath(fn)
  with open(dn) as f:
    data = yaml.safe_load(f)
    subloadYaml(data)
    return data


def WriteYaml(fn, obj):
  '''
  Write a dict object to a *.yaml file in the "data" folder.
  '''
  dn = GetDataPath(fn)
  dir = os.path.dirname(os.path.abspath(dn))
  os.makedirs(dir, exist_ok=True)
  with open(dn, 'w') as f:
    yaml.dump(obj, f)


def GetDataPath(fn):
  '''
  @fn is a relative path; e.g. "x.txt" or "mystuff/x.txt"
  This function defines where these data items are to be stored;
  currently in the "data/" folder, but we might change it later.
  '''
  return os.path.join("data", fn)


def DataFileExists(fn):
  return os.path.exists(GetDataPath(fn))


def YN(prompt='', default=True):
  'Prompt for yes or no. Return boolean'
  a = input(prompt).upper()[:1]
  if a == '': return default
  if a == 'Y': return True
  if a == '1': return True
  if a == 'T': return True
  return False




class ToolsTests(unittest.TestCase):
  def test_Fluid(self):
    # Pick some useful YAML string that might cover a bunch of tests.
    o = ParseYaml('''
animals: [bird, dog, cat]
fred:
  first: "Fred"
  last: "Flintstone"
wilma:
  first: "Wilma"
  last: "Flintstone"
states:
  - name: Arizona
    capital: Phoenix
  - name: California
    capital: Sacremento
  - name: New York
    capital: Albany
pets:
  cat:
    sounds: 
      - meow
      - purr
    verbs:
      - sleep
      - eat
      - chase
  dog:
    sounds:
      - bark
      - woof
      - howl
    verbs:
      - sleep
      - eat
      - sniff
    ''')

    # Create a Fluid object from the YAML
    f = Fluid(o)

    # Test some accessors
    self.assertEqual("dog", f.animals[1])
    f.animals[9] = "rabbit"
    self.assertEqual(None, f.animals[8])
    self.assertEqual("rabbit", f.animals[9])
    with self.assertRaises(IndexError):
      f.animals[10]

    self.assertEqual("Fred", f.fred.first)
    self.assertEqual("Flintstone", f.fred.last)
    self.assertEqual("Wilma", f.wilma.first)
    self.assertEqual("Arizona", f.states[0].name)
    self.assertEqual("Phoenix", f.states[0].capital)
    self.assertEqual("New York", f.states[2].name)
    self.assertEqual("Albany", f.states[2].capital)

    f.states[2].capital = "Whatever"
    self.assertEqual("Whatever", f.states[2].capital)

    # Enumerate some list
    s = ','.join([str(x) for x in f.pets.dog.sounds])
    self.assertEqual("bark,woof,howl", s)
    self.assertEqual("", str(f.pets.dog.sounds))
    self.assertEqual("", repr(f.pets.dog.sounds))


  def test_FluidNew(self):
    f = Fluid()
    f[5] = "Hi"
    f[2] = {}
    f[2].color = "Orange"
    f[2].taste = "Yummy"
    #f[2].properties = {}
    f[2].properties.weight = 10
    f[2].properties.shape = 'round'
    print(f)
    self.assertEqual("""
- null
- null
- color: Orange
  properties:
    shape: round
    weight: 10
  taste: Yummy
- null
- null
- Hi
    """.strip(), str(f).strip())

  def test_WriteFluid(self):
    data = ParseYaml("numbers: [1,2,3]")
    WriteYaml("testwritedata", data)


if __name__ == '__main__':
  unittest.main()
