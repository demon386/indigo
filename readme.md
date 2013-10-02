# Indigo -- Python clone of Plumbing, framework for structued computation

Author: M. Tong (demon386@gmail.com)

Indigo is a clone of [Plumbing](https://github.com/Prismatic/plumbing) (by Prismatic) in Python. Both of its interface and implementation are highly inspired by Plumbing.

The objective of Indigo is to make structued computation easier in Python.

The following is an example from [Plumbing](https://github.com/Prismatic/plumbing) github page translated to Indigo for calculating variance of an array:
```{python}
import numpy as np
from indigo.graph import compile_graph

graph = {"n": lambda xs: len(xs),
         "m": lambda xs, n: xs.sum() / float(n),
         "m2": lambda xs, n: (xs * xs).sum() / float(n),
         "v": lambda m, m2: m2 - m * m}

graph_func = compile_graph(graph)
xs = np.arange(10)
# Must supply keyword arguments here
graph_func(xs=xs) # {'v': 8.25, 'm2': 28.5, 'm': 4.5, 'n': 10}
```

`v` depends on `m` and `m2`; `m`, `m2` depends on `xs` and `n`; `n` depends on `xs` (the input to the graph). Indigo enables you to describe the dependency painlessly. It will arrange the computation for you.

Right now the library is still in its alpha. There are many exciting features I want to implement:
- Supporting profiling each computation.
- Supporitng parallizing computations, both locally and remotely.
