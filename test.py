# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def MissInformation(G,mainNode):#转发链断裂处理
    for i in G.nodes():
        if G.in_degree(i)==0 and i !=mainNode:
            G.add_edge(mainNode,i)
    return G
def OneMicroblog(mainNode):# 提取一条微博信息
    output = open('F:/github/WoLongBigData/DataManager/weibo'+mainNode+'.txt', 'w+')
    with open('F:/Document/MicroBlogPredict/trainRepost.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            print t[0]
            if t[0] == mainNode:
                output.writelines(line)
    output.close()

# #一条微博信息的转发网络
# G = nx.DiGraph()
# with open('F:/github/WoLongBigData/DataManager/weibo3794305741726764.txt', 'r') as f:
#     for position, line in enumerate(f):
#         t= line.strip().split('\001')
#         G.add_node(t[2],time=t[3],content=t[4])
#         G.add_edge(t[1],t[2])
# G = MissInformation(G,'2724513')
# nx.draw(G)
# plt.savefig("Picture/weibo3794305741726764.png")
# plt.show()

#一条微博信息的传播深度和传播广度与时间曲线
G = nx.DiGraph()
width=[0]*300
depth=['']*300
with open('F:/github/WoLongBigData/DataManager/weibo3794305741726764.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\001')
        G.add_node(t[2],time=int(t[3]),content=t[4])
        G.add_edge(t[1],t[2])
G = MissInformation(G,'2724513')
time = nx.get_node_attributes(G,'time')
for i in time:
    if time[i]/900 < 288:
        width[(time[i]/900)+1]=width[(time[i]/900)+1]+1
        depth[(time[i]/900)+1]=depth[(time[i]/900)+1]+i+'\001'
for i in range(width.__len__()-1):
    width[i+1] =width[i+1]+width[i]
x=range(300)
plt.plot(x,width,color='r')#转发规模随时间变化
plt.savefig("Picture/weibo3794305741726764Width.png")
plt.show()
temp=['2724513']
for i in range(depth.__len__()):
    if depth[i]!=0 :
        temp = temp+depth[i].split('\001')[:-1]
        NG=MissInformation(G.subgraph(temp),'2724513')
        depth[i]=nx.eccentricity(NG.to_undirected())['2724513']
        print depth[i]
plt.plot(x,depth,color='r')#转发深度随时间变化
plt.savefig("Picture/weibo3794305741726764Depth.png")
plt.show()

