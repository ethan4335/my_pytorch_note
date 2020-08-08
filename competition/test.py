#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_pytorch_note'
__author__ = 'deagle'
__date__ = '8/4/2020 21:34'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
from random import sample
import random

def main():
    print(sample(random(0,25),5))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    time_cost = end_time - start_time
    print(str(time_cost).split('.')[0])
