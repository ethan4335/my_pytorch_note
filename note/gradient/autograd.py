#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pytorch_note'
__author__ = 'deagle'
__date__ = '7/24/2020 10:53'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import torch

#torch.Tensor 是这个包的核心类。如果设置它的属性 .requires_grad 为 True，那么它将会追踪对于该张量的所有操作。

import torch
#创建一个张量并设置requires_grad=True用来追踪其计算历史
x = torch.ones(2, 2, requires_grad=True)
print(x)
y = x + 2
print(y)

print(y.grad_fn)

z = y * y * 3
out = z.mean()

print(z, out)

if __name__ == '__main__':
    print()