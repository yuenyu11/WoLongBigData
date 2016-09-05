# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
Wid='3794305741726764'
output=open('F:/Document/MicroBlogPredict/weiboTest.txt', 'w+')
with open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'relationship.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\t')
        if t.__len__()>1:
            for i in t[1].split('\001'):
                output.writelines(t[0]+','+i+'\n')



# for i in G.nodes():
