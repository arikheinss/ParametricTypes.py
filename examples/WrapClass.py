# ignore this shit here...
import sys
import os
base, _ = os.path.split(__file__)
sys.path.append(os.path.abspath(os.path.join(base, "..")))


# this is the example
from typing import TypeVar
from src.parametrictypes import ParametricClass



T = TypeVar("T")

class wrapper[T](metaclass = ParametricClass):

    def __init__(self, x: T):
        self.set(x)

    def set(self, v: T):
        if not isinstance(v, T):
            raise TypeError(f"wrapper of type ({T}) got value of type {type(v)}")
        self.data = v

    def get(self) -> T:
        return self.data
# =============================================
    
w_int = wrapper[int](2)

w_int.set(4)
print(w_int.get()) # 4

w_int.set("hello") # error!!
w_2 = wrapper(None) # error!! Missing type parameters!!