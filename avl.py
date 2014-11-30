# -*- coding: utf-8 -*-

from binarysearchtree import bst
from binarysearchtree import node

class avl(bst):
    
    def __init__(self,node = None):
        bst.__init__(self,node)
        
    def insert(self,k,p = None):
        bst.insert(self,k,p)
        
        
        
    def checkinvariant(self):
        bst.findheights(self)      
        def traverse(node):
            if node!= None:
                if node.left != None and node.right != None:
                    if abs(node.left.height - node.right.height) > 1:
                        return True
                traverse(node.left)
                traverse(node.right)
                return False
        return traverse(self.root)
    
    def leftrotate(self,node):
        
        if node.right.left != None:
            newright = self.lefttree(node.right)            
        node.

        
    '''   
    def balance(self):
        violatingnode
        def traverse(node):
            if node != None:
                if node.left != None and node.right != None:
                    if abs(node.left.height - node.right.height) > 1:
    '''

    
tree = avl()
tree.insert(25)
tree.insert(27)
tree.insert(33)
tree.insert(1)
tree.insert(37)



tree2 = avl()
tree2.insert(12)
tree2.insert(11)
tree2.insert(10)

tree.inserttree(tree2)

print tree

print tree2.root.left

tree3 = tree2.lefttree()
print tree3
