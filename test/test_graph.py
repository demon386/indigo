import numpy as np

from indigo.graph import compile_graph

def test_simple_graph():
    graph = {"n": lambda xs: len(xs),
             "m": lambda xs, n: xs.sum() / float(n),
             "m2": lambda xs, n: (xs * xs).sum() / float(n),
             "v": lambda m, m2: m2 - m * m}

    graph_func = compile_graph(graph)
    xs = np.random.rand(10)
    n = len(xs)
    m = xs.sum() / float(n)
    m2 = (xs * xs).sum() / float(n)
    v = m2 - m * m

    res = graph_func(xs=xs)
    assert res == {"n": n, "m": m, "m2": m2, "v": v}
