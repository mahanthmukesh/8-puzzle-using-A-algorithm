# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from node import Node
from node import Puzzle
from node import Distance


heuristic = input("Choose a Heuristic: \n 1. Misplaced Tiles \n 2. Manhattan Distance \n")
heuristic=int(heuristic)

initial_board=[]
final_board=[]

print("Enter the 8 puzzle problem: \n")

for i in range(9):
    x = int(input())
    initial_board.append(x) 
    
print("Enter the 8 puzzle goal: \n")

for i in range(9):
    x = int(input())
    final_board.append(x) 

initial_board   =   Node(initial_board)
final_board     =   Node(final_board)
explored_nodes  =   []
fringe          =   [initial_board]
distance        =   Distance.distance(initial_board.get_current_state(),final_board.get_current_state(),heuristic)
fringe[0].update_hn(distance)
count=1

print("---------------Printing Solution Path---------------\n \n")

while not not fringe:
    minimum_fn_index    =   Puzzle.least_fn(fringe)
    current_node        =   fringe.pop(minimum_fn_index)
    g                   =   current_node.get_gn()+1
    goal_node           =   np.asarray(final_board.get_current_state())
    if np.array_equal(np.asarray(current_node.get_current_state()), goal_node ):
        distance    =   Distance.distance(np.asarray(current_node.get_current_state()),goal_node,heuristic)
        explored_nodes.append(current_node)
        Puzzle.goal_reached(explored_nodes,count)
        fringe      =   []
    elif not np.array_equal(current_node, goal_node ):
        zero    =   np.where(np.asarray(current_node.get_current_state()) == 0)[0][0]
        count   =   Node.expand_node(fringe, explored_nodes, current_node,goal_node, zero, g, count,heuristic)

