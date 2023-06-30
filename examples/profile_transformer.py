'''
Author: Beta Cat 466904389@qq.com
Date: 2023-06-25 20:24:22
LastEditors: Beta Cat 466904389@qq.com
LastEditTime: 2023-06-30 17:31:06
FilePath: /GT2023/torchprofile/examples/profile_transformer.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import torch
from torch.nn.modules.transformer import Transformer
from torchprofile import profile_macs

if __name__ == '__main__':
    embed_size = 512
    num_tokens = 30

    model = Transformer(embed_size)
    inputs = (
        torch.randn(num_tokens, 1, embed_size),
        torch.randn(num_tokens, 1, embed_size),
    )

    # macs = profile_macs(model, inputs)
    # print('transformer: {:.4g} G'.format(macs / 1e9))
    df,op_df = profile_macs(model, inputs,reduction=None)
    for item in op_df:
        print(item)
    # for key,value in macs.items():
    #     print("key:   ",key)
    #     print("value:   ",value)
