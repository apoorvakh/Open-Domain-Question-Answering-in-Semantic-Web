"""
nsubjpass(married-3, Who-1)
auxpass(married-3, was-2)
root(ROOT-0, married-3)
nmod(married-3, to-4)
det(actor-6, an-5)
dep(to-4, actor-6)
nsubj(starred-8, actor-6)
ref(actor-6, that-7)
acl:relcl(actor-6, starred-8)
nmod(starred-8, in-9)
dep(in-9, Philly-10)
"""

import networkx as nx
import pylab as plt
import pickle
from fuzzywuzzy import process,fuzz
#import semantic_sim
from treelib import Tree,Node
from operator import itemgetter
from collections import defaultdict

#para_dict = pickle.load(open('para_dict.p','r'))

def get_list(file):
    file.seek(0)
    list = []
    for i in file:
        list.append(i[:-1])
    return list

def getNodes(txt):
    words = txt.replace('(','$').replace(')','$').replace(', ','$').split('$')
    #print words
    return words


### gets the root to begin with ###
def getRoot(tree,list):
    for i in list:
        words = getNodes(i)
        if words[0]=="root":
            #print "root found",words #works
            tree.create_node(words[2],words[2],data="root")
            #tree.show()
            return words

### gets the next node for a particular word ###
def getNextNode(tree,list,done_dict,word_check):
    #print "done(getNextNode)",done_dict.items()

    for i in done_dict.items():
        #print "I",i[0]
        if done_dict[i[0]]['done']==True:
            for j in done_dict[i[0]]['child']:
                #print "J",j
                if done_dict[j]['done']==False:
                    #print "returning ",j
                    return j
    return None




def addNodes(tree,list,done_dict):
    list_2b_checked = getRoot(tree,list)
    word_child=list_2b_checked[2]
    done_dict[word_child] = {"done":False,"child":[]}
    #print "word child     ",word_child
    while word_child!=None:
       # print "\n\n######LOOP DONE##########\n\n"
        for i in list:
            words=getNodes(i)
            if (list_2b_checked != words) and words[1]==word_child and words[0]!='ref':
               #print "parent,wrsd[0]   ",words[1],words[0]
               if tree.parent(words[1])!=None and (tree.parent(words[1])).identifier==words[2]:
                  #print "parent,2   ",words[1],(tree.parent(words[1])).identifier
                  x=refTree[words[2]]
                  #print "X  ",x
                  tree.create_node(words[2],x,parent = words[1],data=words[0])
                  #print "node added!\n",tree.show()

               else:
                    tree.create_node(words[2],words[2],parent = word_child,data=words[0])
                    done_dict[word_child]['child'].append(words[2])
                    done_dict[words[2]]= {"done":False,"child":[]}
                   # print "node added!\n",tree.show()
            elif  (list_2b_checked != words) and words[1]==word_child :
                  refTree[word_child]=words[2]

        done_dict[word_child]['done']=True
        word_child = getNextNode(tree,list,done_dict,word_child)


############### test ####################

#print "start"
tree= Tree()
refTree={}
done_dict = defaultdict(list)

file=open('treefinal1.txt')
list = get_list(file)
#print "list ",list

addNodes(tree,list,done_dict)
print "\n ########## FINAL ############# \n"
tree.show()





