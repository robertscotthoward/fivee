# Overview
Fivee (or 5e or 5th Edition) is a python engine for simulating 
Dungeons & Dragons Fifth Edition (D&D 5e) scenarios, encounters, 
and melee attacks.

The data that drives this simulator is defined in a YAML file (`data/data.yaml`) 
that can (for organizational convenience) contain references 
to other YAML files. Wherever an object contains property `ref`, 
the value is assumed to refer to a sibling file, which is read in at
runtime; much like an "include" statement. 
This way, a single YAML file can be spread out over many files.

# Unit Tests
To run all unit tests, run `tests.py`. You can set breakpoints in Visual Studio.

Or from the command line run:
`python -m unittest`

# Definitions

## Player
A player character (PC) is an Actor that is prompted for choices. A non-player character (NPC) is 
an Actor that the computer makes choices for when its turn arises. Monsters are NPCs, but typically 
without names.

## Turns
Each player is presented in turns. The next player gets a description of the surroundings, state
of the environment, and allowed to perform certain tasks. Then the turn completes, the next player
starts its turn. This repeats forever.

This can get a bit tiresome. Thus players can be banded together into a "party" that is 
presented the same surroundings once, for all players, and then the party is treated as a 
single player. Only when the party encouters an enemy does the engine split the players 
(temporarily) into individuals who make individual decisions together.

## Party
A party is a collection of PCs that follow the leader by default. That is, they move together and 
search together, and split treasures together.

## Melee
A melee occurs when a party encounters a foe. Then each player is prompted for each choice in the
game; i.e. what to do, where to go, when to fight or flee, etc.

# Usage
Run file `main.py`. This does the following:

## Read data.yaml file
The file is recursively read into a single YAML file, and 
then converted to a [Fluid](fluid.md) object. 

## Load campaign
A campaign is a yaml file under the `campaigns` folder. 
You can create a new campaign (and name it) or load an existing
campaign by name. A campaign contains the current state of these components:
* Environment: continents, kindgoms, places, cities, keeps, castles, pubs, doors, traps, etc.
* Players: PC, NPC, Monsters
* Items: magic items, weapons, equipment, treasures - things that can be moved.

* Thing
  * Has position, but can be inside another thing, and assume its position.
  * Has weight
  * Has cost
  * Has owner
  * Has other states

* Static : Thing
  * Position is fixed
  * Weight is infinite, but can be destroyed.

* Dynamic : Thing
  * Can be moved. Position varies by external forces.

* Actor : Dynamic
  * Takes turns
  * Makes decisions
  * Has hit points. Can die.

## Managed the state evolution of the campaing
That is, it does the following in a loop:

* Determines which possible things can be done from the current state; i.e. the transitions (or edges in a graph).
* Allows the party (or each member) the option to select which of the possible choices to do.
* Executes the outcome of the options and displays it.


