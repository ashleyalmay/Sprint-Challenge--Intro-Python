# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for h in humans:
    if h.name.startswith('D'):
        a.append(h.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for h in humans:
    if h.name.endswith('e'):
        b.append(h.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for h in humans:
    if h.name[0] in ['C','D','E','F','G']:
        c.append(h.name)
print(c)


# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [a.age + 10 for a in humans]
    #ref 11_args.py


print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [F'{h.name}-{h.age}'for h in humans]
print(e)
#ref to 04_printing.py


# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(h.name, h.age)for h in humans if 32>= h.age >=27]
print(f)
#ref 06_tuples.py

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(h.name.upper(), h.age + 5) for h in humans]
print(g)

#ref 08_comprehensions.py + adding 5 to the age

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(h.age) for h in humans]
print(h)
