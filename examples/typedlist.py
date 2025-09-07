
# ignore this shit here...
import sys
import os
base, _ = os.path.split(__file__)
sys.path.append(os.path.abspath(os.path.join(base, "..")))


# this is the example
#=========================================================================
#=========================================================================
from typing import TypeVar
from src.parametrictypes import ParametricClass
T = TypeVar("T")



class TypedList[T](metaclass = ParametricClass):

    def __init__(self, data = None):
        self.data = data or []

    def __setitem__(self, i: int, v: T):
        if not isinstance(v, T):
            raise TypeError(f"List of type ({T}) got key of type {type(v)}")
        self.data[i] = v

    def __getitem__(self, i: int) -> T:
        return self.data[i]
    
    def append(self, v: T):
        if not isinstance(v, T):
            raise TypeError(f"List of type ({T}) got key of type {type(v)}")
        self.data.append(v)


    def __str__(self):
        return f"{T}{self.data}"
#=========================================================================
#=========================================================================

l_int = TypedList[int]([0, 0])
l_int[0] = 1
l_int[1] = 11
print(l_int) # <class 'int'>[1, 11]



try:
    l_int[1] = "hello"
except Exception as e:
    print("Got Exception: ", e)

# Got Exception:  List of type (<class 'int'>) got key of type <class 'str'>

try: 
    l = TypedList()
except Exception as e:
    print("Got Exception: ", e)
# Got Exception:  cannot instantiate Typeclass without parameters


l2 = TypedList[int]()
print("subtypes TypedDict: ", isinstance(l_int, TypedList)) # True
print("is a Typed Dict: ", type(l_int) is TypedList) # False
print("Types are identical within parameters", type(l2) is type(l_int)) # True

l_str = TypedList[str]()
print("Types are identical acros parameters", type(l_str) is type(l_int)) # False


class A():pass
class B(A): pass

l_a = TypedList[A]()
l_b = TypedList[B]()
print("Types are covariant: ", isinstance(type(l_b), type(l_a))) # False

b = B()
l_a.append(b)
print(l_a) # <class '__main__.A'>[<__main__.B object at 0x0000022D7E695190>]
# in other words: subclasses are respected by type params