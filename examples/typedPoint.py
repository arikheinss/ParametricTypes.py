# ignore this shit here...
import sys
import os
base, _ = os.path.split(__file__)
sys.path.append(os.path.abspath(os.path.join(base, "..")))


# this is the example
from typing import TypeVar
from src.parametrictypes import ParametricClass, CheckedParametric



T = TypeVar("T")

class point[T](metaclass = CheckedParametric):
    x: T  
    y: T 
    def __str__(self):
        return f"point[{T}]({self.x}, {self.y})"

import math
sqr = lambda x: x* x

class line[T](metaclass = CheckedParametric):
    start: point[T]
    end: point[T]
    length: T | float  # this makes not really sense, just trying out the type system
    def __init__(self, p1, p2):
        self.start = p1 
        self.end = p2 
        self.length = math.sqrt(sqr(p1.x - p2.x) + sqr(p1.y - p2.y))


print(point.__annotations__)
print(point[int].__annotations__)

print(line.__annotations__)
print(line[int].__annotations__)

p = point[int]()
p.x = 2
p.y = 0
print(p)

try:
    p.x = 0.5
    print(p)
except Exception as e:
    print("caught: ", e)

p2 = point[int]()
p2.x = 1
p2.y = 1

l = line[int](p, p2)
print(l)

p_f = point[float]()

try:
    l.start = p_f
    print(p)
except Exception as e:
    print("caught: ", e)