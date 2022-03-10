# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:38:53 2021

@author: Ariel
"""

my_list = [1,23,4,5,6,1,2,4]

#Make a linked list implementation


class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
        
    def printval(self):
        return print(self.dataval)
        
class LinkedList:
    def __init__(self):
        self.head = None
        

        

llist1 = LinkedList()

llist1.head = Node('Churro')

node2 = Node("papito")
node3 = Node('Major')
node4 = Node('John Wish')
node5 = Node("Pluck")


llist1.head.nextval = node2

node2.nextval = node3
node3.nextval = node4
node4.nextval = node5
