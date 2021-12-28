from fluid import Fluid
from tools import *
import os
import yaml
data = {}
campaign={}

# Load the data.yaml into memory
data = Fluid(ReadYaml("data.yaml"))


def CreateCampaign(name):
  '''
  Create a default campaign and store it in the folder.
  A campaign is snapshot of an environment plus the states of the characters.
  '''
  campaign = {
    "name": name
  }

  return campaign

def ChooseCampaign():
  while True:
    name = input("Which campaign: ")
    fn = f"campaigns/{name}.yaml"
    if DataFileExists(fn):
      return Fluid(ReadYaml(fn))
    if not YN("Campaign does not exist. Create it? [y]: "):
      continue

    camp = CreateCampaign(name)
    WriteYaml(fn, name)
    return camp


ChooseCampaign()
