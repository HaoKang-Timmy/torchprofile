'''
Author: Beta Cat 466904389@qq.com
Date: 2023-06-25 20:24:22
LastEditors: Beta Cat 466904389@qq.com
LastEditTime: 2023-06-30 17:42:50
FilePath: /GT2023/torchprofile/examples/trace_linear.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torch
import torch.nn as nn
from torchprofile.utils.trace import trace
from torchprofile import profile_macs

if __name__ == '__main__':
    in_features = 16
    out_features = 32

    model = nn.Linear(in_features, out_features)
    inputs = torch.randn(1, in_features)
    _,df = profile_macs(model, inputs,reduction=None)
    print(df)
    # graph = trace(model, inputs)
    
    # print(graph)
