#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lirun
# datetime:2018/9/30 11:08
# software: PyCharm

import torch
import numpy as np

x = torch.from_numpy(np.arange(4).reshape((1, 4)))

print('tensor原型:', x)

print('x沿着维度0复制2倍', np.tile(x, 2))
print('x沿着维度0、维度1，分别复制2倍、2倍', np.tile(x, (2, 2)))
print('x沿着维度0、维度1、维度2，分别复制2倍、2倍、2倍', np.tile(x, (2, 2, 2)))









