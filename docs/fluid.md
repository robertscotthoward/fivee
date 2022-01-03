# Fluid Object
A Fluid object is an object that wraps a dict/list composite; i.e. one
that is returned from a `yaml.safe_load(file)` call.

But suppose that `f` is a variable that represents a dict of
dict objects. Then you would access the values in a manner such 
as this example:
```python
f = tools.ReadYaml("data.yaml")
first = f["people"][3]["firstname"]
childfirst = f["people"][3]["children"][2]["firstname"]
```

With the Fluid object, you can do this (much like JavaScript):
```python
f = Fluid(tools.ReadYaml("data.yaml"))
first = f.people[3].firstname
childfirst = f.people[3].children[2].firstname
```

It is the authors opinion that this is easier to read.

You can even add properties that were not there before to build
structures dynamically:

```python
f = Fluid()
f.people = []

f.people += {}
f.people[-1].first = "Fred"
f.people[-1].last = "Flintstone"
f.people[-1].pets = []
f.people[-1].pets += "Dino"
f.people[-1].pets += "Baby Puss"

f.people += {}
f.people[-1].first = "Barney"
f.people[-1].last = "Rubble"

# Find a record

print(str(f))
```

Returns:
```yaml
people:
- first: Fred
  last: Flintstone
  pets:
  - Dino
  - Baby Puss
- first: Barney
  last: Rubble
```

