# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:46:14 2022

@author: siava
"""

class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        # pointer to parent node in tree
        self.parent = None
        
        
class BST(object):
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root == None:
            self.root=Node(value)
        else:
            self._insert(value,self.root)
    # _insert funscion is a private recursive function
    def _insert(self,value,current_Node):
        if value < current_Node.value:
            if current_Node.left_child == None:
                current_Node.left_child = Node(value)
                # set parent
                current_Node.left_child.parent=current_Node 
            else:
                self._insert(value,current_Node.left_child)
                
        # if the value is gretaer than the value of the current Node
        if value > current_Node.value:
            if current_Node.right_child == None:
                current_Node.right_child = Node(value)
                current_Node.right_child.parent=current_Node # set parent
            else:
                self._insert(value,current_Node.right_child)
                
        # The case where the value is equal to the current Node
        else:
            print ("you fool! the value is already in tree")
            
            
    def display_tree(self):
        if self.root !=None:
            self._display_tree(self.root)
            
    def _display_tree(self,current_Node):
        if current_Node !=None:
            self._display_tree(current_Node.left_child)
            print(str(current_Node.value))
            self._display_tree(current_Node.right_child)

    def height(self):
        if self.root!=None:
             return self._height(self.root,0)
        else:
             return 0
         
    def _height(self, current_Node, current_height):
        if current_Node ==None:return current_height
        left_height=self._height(current_Node.left_child,current_height+1)
        right_height=self._height(current_Node.right_child,current_height+1)
        return max(left_height,right_height)

    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False
        
    def _search(self,value,current_Node):
        if value==current_Node.value:
            return True
        elif value<current_Node.value and current_Node.left_child!=None:
            return self._search(value,current_Node.left_child)
        elif value>current_Node.value and current_Node.right_child!=None:
            return self._search(value,current_Node.right_child)
        return False 
    
    
    # return the node with the specified input value
    # returns true if it exists in the tree
    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None	
        
    def _find(self,value,current_Node):
        if value==current_Node.value:
            return current_Node
        elif value<current_Node.value and current_Node.left_child!=None:
            return self._find(value,current_Node.left_child)
        elif value>current_Node.value and current_Node.right_child!=None:
            return self._find(value,current_Node.right_child)
        
    def delete_value(self,value):
        return self.delete_node(self.find(value))

    def delete_node(self,Node):
        
        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current
        
        # returns the number of children for the specified node
        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children
        
        # get the parent of the node to be deleted
        Node_parent = Node.parent

		# get the number of children of the node to be deleted
        Node_children=num_children(Node)
        
        
        
    
        # break operation into different cases based on the
		# structure of the tree & node to be deleted

		# CASE 1 (node has no children)
        if Node_children==0:

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
            if Node_parent!=None:
				# remove reference to the node from the parent
                if Node_parent.left_child==Node:
                    Node_parent.left_child=None
                else:
                    Node_parent.right_child=None
            else:
                self.root=None

		# CASE 2 (node has a single child)
        if Node_children==1:

			# get the single child node
            if Node.left_child!=None:
                child=Node.left_child
            else:
                child=Node.right_child

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
            if Node_parent!=None:
				# replace the node to be deleted with its child
                if Node_parent.left_child==Node:
                    Node_parent.left_child=child
                else:
                    Node_parent.right_child=child
            else:
                self.root=child

			# correct the parent pointer in node
            child.parent=Node_parent

		# CASE 3 (node has two children)
        if Node_children==2:

			# get the inorder successor of the deleted node
            successor=min_value_node(Node.right_child)

			# copy the inorder successor's value to the node formerly
			# holding the value we wished to delete
            Node.value=successor.value

			# delete the inorder successor now that it's value was
			# copied into the other node
            self.delete_node(successor)
    
def fill_tree(tree, num_elements=100, max_int=1000):
    from random import randint
    for i in range(num_elements):
        current_element = randint(0,max_int)
        tree.insert(current_element)
    return tree



#Test the above code with some examples
tree = BST()
tree = fill_tree(tree)
tree.display_tree()
print ("tree height is:",tree.height())


tree1 = BST()
tree1.insert(5)
tree1.insert(1)
tree1.insert(3)
tree1.insert(2)
tree1.insert(7)
tree1.insert(10)
tree1.insert(0)
tree1.insert(20)

tree1.display_tree()
print ("tree height is:",tree1.height())
print (tree1.search(10))
print (tree1.search(30))


tree2 =  BST()
tree2.insert(5)
tree2.insert(4)
tree2.insert(6)
tree2.insert(10)
tree2.insert(9)
tree2.insert(11)
tree2.display_tree()
tree2.delete_value(5)
tree2.display_tree()




        