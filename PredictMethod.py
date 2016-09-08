# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'

import graphlab
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def MissInformation(G,mainNode):#转发链断裂处理
    for i in G.nodes():
        if G.in_degree(i)==0 and i !=mainNode:
            G.add_edge(mainNode,i)
    return G

def FollowerRT(G,G_Relation):#转发来自粉丝的比例(0.71)
    sumF=0.0
    sum=0.0
    n=0
    for i in G.edges():
        sum=sum+1.0
        if G_Relation.has_edge(i[0],i[1]):#是否来源于粉丝
            sumF=sumF+1.0
    return sumF/sum

graphlab.product_key.set_product_key('4042-EE8D-C6AE-8041-2A9E-D542-5EF3-7D88')
G = nx.DiGraph()
G_Relation = nx.DiGraph()
Wid='3794305741726764'
mainNode='2724513'
#构建关系网络
with open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'relationship.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\t')
        if t.__len__()>1:
            for i in t[1].split('\001'):
                G_Relation.add_edge(i,t[0])
# edges =graphlab.SFrame.read_csv('F:/Document/MicroBlogPredict/weibo_dc_parse2015_link_filter_follower.txt',header=False,column_type_hints=[str,str])
# print G_Relation
# G_Relation = graphlab.SGraph()
# G_Relation = G_Relation.add_edges(edges, src_field='X1', dst_field='X2')
#构建转发网络
with open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\001')
        G.add_node(t[2],time=int(t[3]),content=t[4])
        G.add_edge(t[1],t[2])
G = MissInformation(G,mainNode)
print FollowerRT(G,G_Relation)
