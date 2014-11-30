# -*- coding: utf-8 -*-
class node:
    
    def __init__(self,key,p=None):
        self.p = p
        self.key = key
        self.right = None
        self.left = None
        self.height = 0
    
    def __str__(self):
        return "Key: "+str(self.key)
        
    def checkparent(self):
        if self.p == None:
            return None
        elif self.p.left == self:
            return "left"
        else:
            return "right"

    def updateheight(self):
        if self.p != None:
            self.p.height = max(self.p.height,self.height+1)
            self.p.updateheight()
    
class bst:
    
    def __init__(self,node=None):
        self.root=node
        if node != None:
            node.p = None
    
    def __str__(self):
        out = ""
        node = self.root        
        def traverse(node,out):
            if node != None:
                out+=str(node)+" "
                traverse(node.left,out)
                out = traverse(node.left,out)
                traverse(node.right,out)
                out = traverse(node.right,out)
            return out
        return traverse(node,out)
    '''
    def findleaves(self):
        self.leaves = []
        node = self.root
        def traverse(node):
            if node != None:
                if node.right == None and node.left == None:
                    self.leaves.append(node)
                traverse(node.left)
                traverse(node.right)
        traverse(node)
        
    def findheights(self):
        self.findleaves()        
        level = self.leaves        
        nextlevel = []
        while len(level)!=0:
            for leaf in level:
                if leaf.p != None:
                    leaf.p.height = max(leaf.p.height,leaf.height+1)
                    if not leaf.p in nextlevel:
                        nextlevel.append(leaf.p)
            level = nextlevel
            nextlevel = []
    '''
    def lefttree(self,node = None):
        if node == None:
            node = self.root
        if node.left != None:
            return bst(node.left)
        
    def righttree(self,node = None):
        if node == None:
            node = self.root
        if node.right != None:
            return bst(node.right)
        
    def insert(self,k,p=None):
        if self.root == None:
            self.root = node(k)
        else:
            if p == None:
                p = self.root
            if p.key >= k:
                if p.left == None:
                    p.left = node(k,p)
                    p.left.updateheight()
                else:
                    self.insert(k,p.left)
            else:
                if p.right == None:
                    p.right = node(k,p)
                    p.right.updateheight()
                else:
                    self.insert(k,p.right)
                    
    def inserttree(self,tree,p = None):
        node = tree.root
        if self.root == None:
            self.root = node
        else:
            if p == None:
                p = self.root
            if p.key >= node.key:
                if p.left == None:
                    p.left = node
                    p.left.updateheight()
                else:
                    self.inserttree(tree,p.left)
            else:
                if p.right == None:
                    p.right = node
                    p.right.updateheight()
                else:
                    self.inserttree(tree,p.right)
    
    def find(self,k,p=None):
        if p == None:
            p = self.root
        if p.key == k:
            return True
        elif p.key > k:
            if p.left == None:
                return False
            else:
                return self.find(k,p.left)
        else:
            if p.right == None:
                return False
            else:
                return self.find(k,p.right)
    
    def findmin(self,node=None):
        if node == None:
            node = self.root
        if node.left == None:
            return node
        else:
            return self.findmin(node.left)
    
    def deletemin(self):
        minnode = self.findmin()
        minnode.p.left = None
         
    def next_larger(self,node):
        if node.right != None:
            return self.findmin(node.right)
        else:
            p = node.p
            while p!=None and node==p.right:
                node = p
                p = node.p
            return p
    
    def delete(self,node):
        p = node.p
        new = self.next_larger(node)
        left = node.left
        right = node.right
        new.p.left = new.right
        if new.right != None:
            new.right.p = new.p
        if node.checkparent() == "right":
            p.right = new
        elif node.checkparent() == "left":
            p.left = new
        new.left = left
        if node.right != new:
            new.right = right
'''        
root = node(12)
tree = bst()
tree.insert(12)
tree.insert(23)
tree.insert(10)
tree.insert(33)
tree.insert(5)
tree.insert(17)

tree.deletemin()

tree.insert(5)
tree.delete(tree.root.right)
tree.insert(1)
tree.findheights()
print tree.root.height


print tree.root.right
print tree.root.right.right
print tree.root.left
print tree.find(23)
print tree.find(18)
print tree.findmin()
print tree.next_larger(tree.root.left.left)
tree.deletemin()
print tree.findmin()
tree.deletemin()
print tree.findmin()
tree.delete(root.right)
'''