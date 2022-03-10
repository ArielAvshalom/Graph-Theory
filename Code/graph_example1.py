# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:27:25 2021

@author: Ariel
"""
import numpy as np

new_graph = np.array([[0,1,1,1,0,0,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,0,0,1,0,1,1], [0,0,0,1,1,0,1], [0,1,1,0,1,1,0]])

new_graph_squared = new_graph @ new_graph

new_graph_cube = new_graph @ new_graph @ new_graph

new_graph_quant = new_graph @ new_graph @new_graph @ new_graph


graph2 = np.array([[0,1,0,1,1,1,1],[1,0,1,1,1,1,1],[0,1,0,1,0,1,1],[1,1,1,0,1,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,0,1],[1,1,1,1,1,1,0]])

graph2_cube = graph2 @ graph2 @ graph2

traced = np.trace(graph2_cube)/6

graph3 = np.array([[0,1,1],[1,0,1],[1,1,0]])

graph3_cubed = graph3 @ graph3 @ graph3

graph4 = np.array([[0,1,1,1], [1,0,0,1], [1,0,0,1], [1,1,1,0]])

graph4_2 = np.array([[0,1,1,0], [1,0,0,1], [1,0,0,1], [0,1,1,0]])

graph4_cube = graph4 @ graph4 @ graph4
graph4_2_cube = graph4_2 @ graph4_2 @graph4_2


graph4_quant = graph4_cube @ graph4
graph4_2_quant = graph4_2_cube @ graph4_2


graph5 = np.array([[0,1,0,0,1], [1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,1],[1,0,0,1,0]])

graph5_5x = graph5@graph5@graph5@graph5@graph5

print(np.trace(graph5_5x))

graph6 = np.array([[0,1,0,0,0,1], [1,0,1,0,0,0], [0,1,0,1,0,0], [0,0,1,0,1,0],[0,0,0,1,0,1],[1,0,0,0,1,0]])

graph6_6x = graph6 @ graph6 @ graph6 @ graph6 @ graph6 @ graph6