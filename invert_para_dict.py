#import findingRel3
import pickle
#from treelib import Tree,Node
from collections import defaultdict



para_dict = pickle.load(open('para_dict.p'))


'''
#extracting the final rel
tree= Tree()
done_dict = defaultdict(list)
file=open('treefinal1.txt')
list = findingRel3.get_list(file)
#print "list ",list
findingRel3.addNodes(tree,list,done_dict)
'''

#pop=getProps(para_dict,tree)



i_dict=defaultdict(list)

for i in para_dict.keys():
    words=i.split()
    for j in words:
        for k in para_dict.keys():
            if j in k:
                i_dict[j].append(k)



print "hi"
pickle.dump(i_dict,open("inverted_index.p",'w'))
