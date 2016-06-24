# coding: utf-8
import numpy as np

class Dijkstra:
    def __init__(self, ver_num, Edges):
        self.dis_list = []
        self.tmp_dis_list = []
        self.S = []
        self.nS = []
        self.p = []
        self.Edges = Edges
        for i in range(ver_num):
            self.p.append(i)
            self.nS.append(i)
            if i == 0:
                self.dis_list.append(0)
                self.tmp_dis_list.append(0)
            else:
                self.dis_list.append(float("inf"))
                self.tmp_dis_list.append(float("inf"))
        print self.nS
        self.count = 0

    def solve(self):
        #繰り返し
        while len(self.nS) >= 1:
            print "{0}回".format(self.count)
            self.count = self.count + 1
            print self.dis_list
            self.v = self.tmp_dis_list.index(min(self.tmp_dis_list))
            self.tmp_dis_list[self.v] = float("inf")
            self.S.append(self.v)
            self.nS.pop(self.nS.index(self.v))
            for j in self.nS:
                self.v = self.S[-1]
                self.a = self.Edges[self.v][j]
                if self.a != 0:
                    if self.dis_list[j] > (self.dis_list[self.v] + self.a):
                        self.dis_list[j] = self.dis_list[self.v] + self.a
                        self.tmp_dis_list[j] = self.dis_list[j]
                        self.p[j] = self.v
        print "最短経路:{0}".format(self.dis_list[-1])
        self.p[0] = float("inf")
        print self.p
