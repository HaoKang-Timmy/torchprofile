'''
Author: Beta Cat 466904389@qq.com
Date: 2023-06-25 20:31:12
LastEditors: Beta Cat 466904389@qq.com
LastEditTime: 2023-06-30 20:26:50
FilePath: /torchprofile/examples/torchprofile/profile.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import warnings

from .handlers import handlers
from .utils.trace import trace
import pandas as pd
import numpy as np
__all__ = ['profile_macs']


def profile_macs(model, args=(), kwargs=None, reduction=sum):
    results = dict()
    op_result_list = []
    graph = trace(model, args, kwargs)
    flag = 0
    for i,node in enumerate(graph.nodes):
        for operators, func in handlers:
            if isinstance(operators, str):
                operators = [operators]
            if node.operator in operators:
                if func is not None:
                    # op_result = dict()
                    # op_result[node.operator] = 
                    results[node] = func(node)
                    op_result = {"Op_name" : node.operator,
                                "Macs" : results[node],
                                "Dimention": node.outputs[-1].shape
                                    }
                    
                    if flag == 0:
                        column = op_result.keys()
                        flag = 1
                    op_result_list.append([op_result[c] for c in column])
                break
        else:
            warnings.warn('No handlers found: "{}". Skipped.'.format(
                node.operator))
    op_result_df = pd.DataFrame(np.array(op_result_list,dtype=object), columns=column, dtype=object)
    if reduction is not None:
        return reduction(results.values())
    else:
        return results, op_result_df
