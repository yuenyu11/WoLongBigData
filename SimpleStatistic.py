# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def MissInformation(G,mainNode):#转发链断裂处理
    temp = nx.connected_components(G.to_undirected())#未连通子图
    for i in temp:
        if i.__contains__(mainNode)==False:
            G.add_edge(mainNode,list(i)[0])
    return G
def OneMicroblog(Wid):# 提取一条微博信息
    output = open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'.txt', 'w+')
    with open('F:/Document/MicroBlogPredict/trainRepost.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            print t[0]
            if t[0] == Wid:
                output.writelines(line)
    output.close()

def HaveRTUser():# 有转发行为的用户
    output = open('F:/github/WoLongBigData/DataManager/HaveRTUser.txt', 'w+')
    s='8381213'
    with open('F:/Document/MicroBlogPredict/trainRepost.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            print t[2]
            if t[2] != s:
                output.writelines(t[2]+'\n')
                s=t[2]
    output.close()
def RTnet(Wid,mainNode):#一条微博信息的转发网络
    G = nx.DiGraph()
    with open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            G.add_node(t[2],time=t[3],content=t[4])
            G.add_edge(t[1],t[2])
    G = MissInformation(G,mainNode)
    nx.draw(G)
    plt.savefig('Picture/weibo'+Wid+'.png')
    plt.show()

def RTWidth(G,Wid):#一条微博信息的累计传播广度
    width=[0]*300
    time = nx.get_node_attributes(G,'time')
    for i in time:
        if time[i]/900 < 288:
            width[(time[i]/900)+1]=width[(time[i]/900)+1]+1
    for i in range(width.__len__()-1):
        width[i+1] =width[i+1]+width[i]
    x=range(300)
    out=open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'Width.txt', 'w+')
    for i in range(len(width)):
        out.writelines(str(1)+'\t'+str(i)+'\t'+str(width[i])+'\n')
    plt.plot(x,width,color='r')#转发规模随时间变化
    plt.savefig('Picture/weibo'+Wid+'Width.png')
    plt.show()

def RTWidthByTime(G,Wid):#一条微博信息的每个时刻（15min）的传播广度
    width=[0]*300
    time = nx.get_node_attributes(G,'time')
    for i in time:
        if time[i]/900 < 288:
            width[(time[i]/900)+1]=width[(time[i]/900)+1]+1
    x=range(300)
    plt.plot(x,width,color='r')#转发规模随时间变化
    plt.savefig('Picture/weibo'+Wid+'AverageWidth.png')
    plt.show()


def RTDepth(G,mainNode):#一条微博信息每时刻的传播深度
    depth=['']*5
    time = nx.get_node_attributes(G,'time')
    for i in time:
        if time[i]/900 < 5:
            depth[(time[i]/900)+1]=depth[(time[i]/900)+1]+i+'\001'
    temp=[mainNode]
    for i in range(depth.__len__()):
        if depth[i]!=0 :
            temp = temp+depth[i].split('\001')[:-1]
            NG=MissInformation(G.subgraph(temp),mainNode)
            depth[i]=nx.eccentricity(NG.to_undirected())[mainNode]
    return depth
    # x=range(300)
    # plt.plot(x,depth,color='r')#传播深度随时间变化
    # plt.savefig('Picture/weibo'+Wid+'Depth.png')
    # plt.show()

def ExtractRelationNetwork(G,Wid):#提取一条微博的关系网络
    output = open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'follower.txt', 'w+')
    with open('F:/Document/MicroBlogPredict/weibo_dc_parse2015_link_filter_follower.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split(',')
            print(t[0])
            if t[0] in G.nodes():
                output.writelines(line)
    output.close()
def FollowerRT(G,G_Relation):#转发来自粉丝的比例(0.71)
    sumF=0.0
    sumF2=0.0
    sum=0.0
    for i in G.edges():
        sum=sum+1.0
        if G_Relation.has_edge(i[1],i[0]):#是否来源于粉丝
            sumF=sumF+1.0
        else:
            for j in G_Relation.in_edges(i[0]):
                if G_Relation.has_edge(i[1],j[0]):#间接粉丝
                    sumF2=sumF2+1.0
    return [sumF/sum,sumF2/sum,(sumF+sumF2)/sum]

def FollowerRatio(G,G_Relation):#转发粉丝/总粉丝
    sumF=0.0
    sum=0.0
    for i in G.edges('2724513'):
        if G_Relation.has_edge(i[1],i[0]):#是否来源于粉丝
            sumF=sumF+1.0

    sum =G_Relation.in_degree('2724513')
    return sumF/sum

def TestWeiBoOneHour():#测试微博一小时转发数据
    out=open('F:/github/WoLongBigData/DataManager/3000WidthOneHours.txt', 'w+')
    s='testWeibo1'
    width=[0]*5
    with open('F:/Document/MicroBlogPredict/testRepostBeforeFirstHour.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            if t[0]==s:
                if int(t[3])<3600:
                    width[(int(t[3])/900)+1]=width[(int(t[3])/900)+1]+1
            else:
                for i in range(width.__len__()-1):
                    width[i+1] =width[i+1]+width[i]
                out.writelines(s+'\t'+str(width[0])+'\t'+str(width[1])+'\t'+str(width[2])+'\t'+str(width[3])+'\t'+str(width[4])+'\n')
                s=t[0]
                width=[0]*5
                if int(t[3])<3600:
                    width[(int(t[3])/900)+1]=width[(int(t[3])/900)+1]+1
    out.close()
def TestDepth():#测试微博的转发深度
    MainNode = nx.DiGraph()
    with open('F:/Document/MicroBlogPredict/WeiboProfile.test', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            MainNode.add_edge(t[0],t[1])
    out=open('F:/github/WoLongBigData/DataManager/3000DepthOneHours.txt', 'w+')
    s='testWeibo1'
    depth=[0]*5
    G = nx.DiGraph()
    with open('F:/Document/MicroBlogPredict/testRepostBeforeFirstHour.txt', 'r') as f:
        for position, line in enumerate(f):
            t= line.strip().split('\001')
            if t[0]==s:
                if int(t[3])<3600:
                    G.add_node(t[2],time=int(t[3]))
                    G.add_edge(t[1],t[2])
            else:
                print s
                mainNode = MainNode.edges(s)[0][1]
                G = MissInformation(G,mainNode)
                p=RTDepth(G,mainNode)
                out.writelines(s+'\t'+str(p[0])+'\t'+str(p[1])+'\t'+str(p[2])+'\t'+str(p[3])+'\t'+str(p[4])+'\n')
                s=t[0]
                depth=[0]*5
                G = nx.DiGraph()
        print s
        mainNode = MainNode.edges(s)[0][1]
        G = MissInformation(G,mainNode)
        p=RTDepth(G,mainNode)
        out.writelines(s+'\t'+str(p[0])+'\t'+str(p[1])+'\t'+str(p[2])+'\t'+str(p[3])+'\t'+str(p[4])+'\n')
    out.close()
G = nx.DiGraph()
# G_Relation = nx.DiGraph()
Wid='3794305741726764'
mainNode='2724513'
with open('F:/github/WoLongBigData/DataManager/weibo'+Wid+'.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\001')
        G.add_node(t[2],time=int(t[3]),content=t[4])
        G.add_edge(t[1],t[2])
G = MissInformation(G,mainNode)

# with open('E:/data/PredictMicroblog/WoLongBigData/DataManager/weibo'+Wid+'relationship.txt', 'r') as f:
#     for position, line in enumerate(f):
#         t= line.strip().split('\t')
#         if t.__len__()>1:
#             for i in t[1].split('\001'):
#                 G_Relation.add_edge(t[0],i)
# print PredictWidth(['2724513'],G_Relation,0.6,0.6)
# print FollowerRatio(G,G_Relation)
RTWidth(G,Wid)





