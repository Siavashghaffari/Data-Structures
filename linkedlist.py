# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:23:28 2020

@author: siava
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linked_list():
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
            
   
        
list1 = linked_list()
list1.head = Node(1)
second = Node(2)
third = Node(3)


list1.head.next = second
second.next = third



list1.display()


