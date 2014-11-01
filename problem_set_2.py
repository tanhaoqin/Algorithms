# -*- coding: utf-8 -*-

"""
Created on Tue Oct 28 18:12:29 2014

@author: Tan Hao Qin
"""

def recursive(i,j):
    if i==j:
        print i
    else:
        print (i,i+(j-i)/2)
        print (i+(j-i)/2+1,j)
        recursive (i,i+(j-i)/2) 
        recursive (i+(j-i)/2+1,j)
    
    
    
recursive(0,19)