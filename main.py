from tools import *
import os
import yaml
data = {}
campaign={}

# Load the data.yaml into memory
data = ReadYaml("data.yaml")

# Pretty-print the data file:
# print(yaml.dump(data, indent=2, default_flow_style=False))

for a in data['abilities']:
  print(f"{a['name']} ({a['abbr'].upper()})")
  if a['abbr'] == 'con':
    print("******************************")


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
      return ReadYaml(fn)
    if not YN("Campaign does not exist. Create it? [y]: "):
      continue

    camp = CreateCampaign(name)
    WriteYaml(fn, name)
    return camp


ChooseCampaign()
