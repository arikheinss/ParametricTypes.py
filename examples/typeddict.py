# ignore this shit here...
import sys
import os
sys.path.append(os.path.abspath("."))



# this is the example
from typing import TypeVar
from src.parametrictypes import ParametricClass

for c in "T W".split():
    globals()[c] = TypeVar(c)


class TypedDict[T, W](metaclass = ParametricClass):
    # like Dict, but with extra typechecks
    def typeparams(self):
        return self.__params__

    def __init__(self):
        self.data = {}

    def __setitem__(self, k: T, v: W):
        if not isinstance(k, T):
            raise TypeError(f"Dict of type ({(T, W)}) got key of type {type(k)}")
        if not isinstance(v, W):
            raise TypeError(f"Dict of type ({(T, W)}) got value of type {type(v)}")
        self.data[k] = v

    def __getitem__(self, k: T) -> W:
        return self.data[k]

    def __str__(self):
        return f"Typesafe Dict[{(T, W)}]: {self.data}"
        

#---------------------------------------------------------------------
#---------------------------------------------------------------------

d_int_to_str = TypedDict[int, str]()
d_int_to_str[2] = "hello"
print(d_int_to_str) # Typesafe Dict[(<class 'int'>, <class 'str'>)]: {2: 'hello'}

try:
    d_int_to_str[3] = False
except Exception as e:
    print("Got Exception: ", e)

# Got Exception:  Dict of type ((<class 'int'>, <class 'str'>)) got value of type <class 'bool'>

try:
    d = TypedDict()
except Exception as e:
    print("Got Exception: ", e)


d2 = TypedDict[int, str]()
print("subtypes TypedDict: ", isinstance(d2, TypedDict)) # True
print("is a Typed Dict: ", type(d2) is TypedDict) # False
print("Types are identical within parameters", type(d2) is type(d_int_to_str)) # True

d_str_to_str = TypedDict[str, str]()
print("Types are identical acros parameters", type(d2) is type(d_str_to_str)) # False

class A():pass
class B(A): pass

d_a = TypedDict[A, A]()
d_b = TypedDict[B, B]()
print("Types are covariant: ", isinstance(type(d_b), type(d_a))) # False

b = B()
d_a[b] = b
print(d_a)
# Typesafe Dict[(<class '__main__.A'>, <class '__main__.A'>)]: {<__main__.B object at 0x000001F63FE54C20>: <__main__.B object at 0x000001F63FE54C20>}
# in other words: subclasses are respected by type params

print(TypedDict.__init__)
