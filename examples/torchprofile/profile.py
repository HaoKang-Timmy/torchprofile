import warnings

from .handlers import handlers
from .utils.trace import trace

__all__ = ['profile_macs']


def profile_macs(model, args=(), kwargs=None, reduction=sum):
    results = dict()
    op_result_df = []
    graph = trace(model, args, kwargs)
    for i,node in enumerate(graph.nodes):
        for operators, func in handlers:
            if isinstance(operators, str):
                operators = [operators]
            if node.operator in operators:
                if func is not None:
                    # op_result = dict()
                    # op_result[node.operator] = 
                    results[node] = func(node)
                    op_result_df.append({node.operator:results[node]})
                break
        else:
            warnings.warn('No handlers found: "{}". Skipped.'.format(
                node.operator))
    if reduction is not None:
        return reduction(results.values())
    else:
        return results, op_result_df
