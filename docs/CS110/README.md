# CS110

## Containers

container is a construct used to group related values together and contains references to other objects instead of data


### String 
* String literal - string value  specified in the source code of a program 

The string type is a special construct known as a sequence type  follows order from left to right 

| Slot 1 |  Slot 2 | Slot 3 | Slot 4 | Slot 5 |
| ------ | ------| ------ | -------|  -----|
| A      | B     | C.     | D      | E     |
| 0      | 1     | 2      | 3      | 4     |


### Lists

* list is a container which holds elements
* elements can different variable type

```python
my_list = [10, 'bw']
print(my_list)
```

#### methods
pop()

remove()

append()

The type of an object also determines the mutability of an object. Mutability indicates whether the object's value is allowed to be changed. Integers and strings are immutable; meaning integer and string values cannot be changed. Modifying the values with assignment statements results in new objects being created and the names bound to the new object

### Tuples

```python
from collections import namedtuple
cs_student = namedtuple('Student',['student_name','student_poe','student_pronouns','student_interests'])
tom_mcclain = cs_student('Tom McClain','Geology','he / him / his','Knot Tying')
print(tom_mcclain)
```

* pair of strings that doesn't change
* tuples cannot be modified.

### Sets 

```python
# Create a set using the set() function.
nums1 = set([1, 2, 3])

# Create a set using a set literal.
nums2 = { 7, 8, 9 }
```
#### Coffee Example

```python 
coffees = set(['americano','latte','espresso'])
print(coffees)

# Add - to set 
coffees.add('cappuccino')
print(coffees)

# sorted() -  sorts the set
print(sorted(coffees))


```

### Dictionaries

Dictionary entries are ordered by position.

A dictionary can provide a map

#### anatomy of dictionary

Curly braces { } are used to build a dictionary.

| object type    | dictionaru       | 
| abbreviated as | dict            |
| consists of    | key - value pair| 

```python 

players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
}

print(players)

# Adds a player and player number
players['Tom McClain'] = 45

print(players)

# Removes a player with the key - 'Tom McClain'
del players['Tom McClain']

print(players)

```