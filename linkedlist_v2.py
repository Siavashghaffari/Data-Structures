# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:23:28 2020

@author: siava
"""

class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class linked_list():
    def __init__(self):
        self.head = Node()
        
                
    def append(self, data):
        New_Node = Node(data)
        cur = self.head
        while (cur.next):
            cur = cur.next
        cur.next = New_Node    
        
        
    def length(self):
        cur = self.head
        total = 0
        while (cur.next):
            total +=1
            cur = cur.next 
        return total
    
    def display(self):
        elems = []
        cur = self.head
        while (cur.next):   
            cur = cur.next
            elems.append(cur.data)
        return elems
    
    def extract(self,index):
        if index >= self.length():
            print("kale kiri index out of range")
            return None
        cur_idx = 0
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur_idx == index:
                return cur.data
            cur_idx +=1
        
    def erase(self,index):
        if index >= self.length():
            print("kale kiri index out of range")
            return None
        cur_idx = 0
        cur = self.head
        while cur.next:
            last = cur
            cur = cur.next
            if cur_idx == index:
                last.next = cur.next
                return
            cur_idx +=1
            

# Thest the above code with some examples
            
list1 = linked_list()


list1.append(4)
list1.append(5)
list1.append(2)
list1.append(3)

list1.display()


print ("the total nodes is: %d" % list1.length())
print ("the nodes are:", list1.display())
print ("element at 2nd index: %d" % list1.extract(2))

list1.erase(1)

print ("the nodes are:", list1.display())
