import os
import yaml


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
