# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.DiGraph()
G_Relation = nx.DiGraph()
Wid='3794305741726764'
mainNode='2724513'
with open('E:/data/PredictMicroblog/WoLongBigData/DataManager/weibo'+Wid+'relationship.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\t')
        if t.__len__()>1:
            for i in t[1].split('\001'):
                G_Relation.add_edge(t[0],i)
print G_Relation.in_degree('272413')

# for i in G.nodes():
