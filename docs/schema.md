# Overview
The `schema.yaml` is a "class" file that defines the structural constraints
of another yaml "object" files. If the object files do not conform to the 
expectations of the class, then a error is raised; which means there
might be a spelling error or misunderstanding in the object file.

# Structure

## Object
An object file is a yaml file that contains a dictionary (or dict or object) of 
property names with corresponding values. Each value can be simple,
such as a string, number, or date; or it can be complex, such as 
a dict, set, or list. Example:

```yaml
people:
  - first: Fred
    last: Flintstone
    age: 33
  - first: Wilma
    last: Flintstone
places:
  countries:
    - name: United States
      abbr: US
      population: 300000000
      capital: Washington DC
      states:
        - name: California
        - name: Arizona
    - name: France
  planets:
    - Mercury: ~
    - Venus: ~
    - Earth: ~
```

`people` and `places` are properties of the object. `people` is a
list property - it contains a list of person objects.

`places` contains one property `countries` that is also a list of
objects.

Each property is a string name (or key) follow by a colon and then a value. 
The value can be a dict, list, set, or simple value -- all defined in the
YAML specification.

`planets` is a list of three objects where the key of each object is a unique 
name of the planet.

## Class (or Schema)
The terms *Schema* and *Class* and *Template* are synonymous. Here is a schema that validates the object above:

```yaml
root:
  type: dict
  properties:
    people:
      type: list
      of: person
    places:
      type: dict
      properties:
        countries:
          type: list
          of: country
    planets:
      type: dict
      of: planet

person:
  type: dict
  properties:
    first:
      type: string
      required: True
    last:
      type: string
      required: True
    age:
      type: integer
      desc: Years old
      required: False

country:
  type: dict
  properties:
    name:
      required: True
    abbr:
      required: True
    population:
      type: integer

```

The schema matches the object's key (e.g. Mercury) one for one.