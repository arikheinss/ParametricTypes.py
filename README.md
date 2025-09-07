
# Parametric Types for python

Do you know this feeling? You _could_ add type parameters to your class, but you feel like it won't matter either way, since they don't really do anything? You wish `myclass[str]` was an actual data type, that you could check against with `isinstance`?

Then ParametricTypes is the package for you! If your class inherits from our `ParametricClass` meta class, your type parameters will become available to you within your code like real variables, to change its behaviour just as you see fit! Additionally, `myclass[int]` now is its own data type, that is distinct from other definitions of `myclass[T]` with other `T`s, but still a subtype of `myclass`! See our examples section for a taste of what it can do.

Get your `ParametricClass` meta class today, and start refactoring your entire code base around it, only here at ParametricTypes.py!



_(ParametricTypes and its owners are not responsible for any potential bugs introduced to your code through our product. Ask your local programmer or software engineer if you encounter unusual behaviour or crashes.)_