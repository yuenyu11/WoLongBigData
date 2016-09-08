# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
Wid='7460165'
with open('F:/Document/MicroBlogPredict/in_degree.txt', 'r') as f:
    s=0
    for position, line in enumerate(f):
        t= line.strip().split(',')
        if t[0] == Wid:
            s=s+int(t[1])
    print s





# for i in G.nodes():
