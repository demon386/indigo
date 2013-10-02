import inspect


class CallableNode(object):
    def __call__(self, *args, **kwargs):
        kwargs = {k: kwargs[k] for k in self.inputs}
        return self.func(**kwargs)


class CallableGraph(CallableNode):
    def __init__(self, g_dict):
        self.output_to_node = {n.output: n for n in g_dict}
        self.orders = self._topological_sort({n.output: n.inputs for n in g_dict})

    def _topological_sort(self, g):
        orders = []
        def dfs(current_node):
            next_nodes = g.get(current_node)
            if next_nodes:
                del g[current_node]
                map(dfs, next_nodes)
                orders.append(current_node)
        while len(g) > 0:
            dfs(g.keys()[0])
        return orders

    def __call__(self, *args, **kwargs):
        output_kwargs = {}
        for output in self.orders:
            node = self.output_to_node.get(output)
            if node:
                res = node(**kwargs)
                kwargs[output] = res
                output_kwargs[output] = res
        return output_kwargs


def compile_graph(g_dict):
    if isinstance(g_dict, CallableNode):
        return g_dict
    elif callable(g_dict):
        return _func_to_node(g_dict)
    else:
        g_dict = [(output, compile_graph(node)) for (output, node) in g_dict.iteritems()]
        g_dict = [_add_output_to_node(output, node) for (output, node) in g_dict]
        return CallableGraph(g_dict)


def _add_output_to_node(output, node):
    node.output = output
    return node


def _func_to_node(func):
    argspec = inspect.getargspec(func)
    args = argspec.args

    node = CallableNode()
    node.inputs = args
    node.func = func
    return node
