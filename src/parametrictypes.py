FunctionType = type(lambda x: x)

def init_throw(self, *args):
    raise Exception(f"cannot instantiate Typeclass without parameters")

def cm(x):
    def closure(y):
        return x + y
    return closure
cl = cm(2)
celltype = type(cl.__closure__[0])

def replace_typevars(f, replacements):
    if (f.__closure__ is None):
        return f
    cell_contents = (c.cell_contents for c in f.__closure__)
    repl = (c if not c in replacements else replacements[c] for c in cell_contents)
    new_cells = tuple(celltype(c) for c in repl)
    return FunctionType(f.__code__, f.__globals__, f.__name__, closure = new_cells)

 
class ParametricClass(type):
    def __init__(self,*args):
        self.cache={}
        self.constructor = self.__init__
        self.__init__ = init_throw 
        
    def __getitem__(self, others):
        if not isinstance(others, tuple):
            others = (others,)
        if not len(self.__type_params__) == len(others):
            raise Exception("wrong number of type params")
        if (cached := self.cache.get(others, None)):
            return cached
        newtype = type(self.__name__, (self,), {"__parameters__" : others, "__init__" : self.constructor})
        newtype.__parameters__ = others
        newtype.__init__ = self.constructor
        
        replacements = {typevar: type for (typevar, type) in zip(self.__type_params__, others)}
        for k in dir(newtype):
            v = getattr(newtype, k)
            if isinstance(v, FunctionType):
                setattr(newtype, k, replace_typevars(v, replacements))
        
        
        self.cache[others] = newtype
        return newtype

    