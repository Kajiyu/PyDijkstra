# coding: utf-8
from Dijkstra import Dijkstra
import numpy as np

if __name__ == '__main__':
    ver_num = 5
    Edges = np.array([[0, 50, 80, 0, 0],
                      [50, 0, 20, 15, 0],
                      [80, 20, 0, 10, 15],
                      [0, 15, 10, 0, 30],
                      [0, 0, 15, 30, 0]])
    d = Dijkstra(ver_num, Edges)
    d.solve()
