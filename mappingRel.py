import findingRel3
import pickle
from treelib import Tree,Node
from collections import defaultdict
from fuzzywuzzy import fuzz

para_dict = pickle.load(open('para_dict.p'))

#extracting the final rel
tree= Tree()
done_dict = defaultdict(list)
file=open('treefinal1.txt')
list = findingRel3.get_list(file)
#print "list ",list
findingRel3.addNodes(tree,list,done_dict)


def getProps(para_dict,tree):
    # using path to leaves get the DFS paths
    # check for tokens
    dict_keys = para_dict.keys()
    print "len ",len(dict_keys)
    paths = tree.paths_to_leaves() #list of lists
    #print "paths  ",paths
    n=0
    properties = {}
    for i in dict_keys: # i is relation phrase from PD
        #print n+1
        n=n+1
        m=0
        for j in paths: # j is a list (in Query)(tree)
            
            #print "Inner for", m+1
            m=m+1
            words = i.split() #words should be subset of j
            #print "going in"
            #print "words   ",words
            #print "j",j

            temp_list=[]
            for k in j:
                temp_list.append((k[:-2]).lower())
                
            #print "t   ",temp_list
            #if temp_list==['married','was']:
             #   print "YES",temp_list
            '''if set(words).issubset(set(temp_list)):
                #print i
                #print para_dict[i]
                return para_dict[i]'''
            length=len(words)
            for small in words:
                if small in temp_list:
                    length=length-1
            if(length==0):
                properties[i]=(para_dict[i])

      
    return properties
    
pop=getProps(para_dict,tree)
#print props








