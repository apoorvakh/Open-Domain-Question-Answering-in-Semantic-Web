from treelib import Tree,Node
import pickle
import findingRel3
from sqlitedict import SqliteDict
wh_list=['who','what','where','which','whom']
print "Opening"
#i_dict=pickle.load(open('inverted_index.p'))
i_dict=SqliteDict("my_db.sqlite",autocommit=True)
print " opened"

def delve(node,inverted_list):
    #print type(node)
    print "Node ",node.identifier
    n_list=tree.children(node.identifier)#.split('-')[0])
    id_list=[]
    remove_list=[]
    for i in n_list:
        if ((i.identifier.split('-'))[0]).lower() not in wh_list:
            id_list.append((i.identifier.split('-')[0]).lower())
        else:
            remove_list.append(i)
    for x in remove_list:
        n_list.remove(x)
    print "id_list ",id_list
    intersect=inverted_list
    if len(id_list)!=0:
        for c in id_list:
            print"C : ",c

            if c in i_dict.keys():
                print" In : C : ",c
                if len(list(set(intersect).intersection(set(i_dict[c]))))==0:
                    return intersect

                elif len(list(set(intersect).intersection(set(i_dict[c]))))>0:
                    intersect=list(set(intersect).intersection(set(i_dict[c])))
                    print "inter    : ",intersect
                else:
                    intersect=delve(n_list[id_list.index(c)],intersect)
                    #return common_list

    else:
        return list(set(intersect).intersection(set(i_dict[(node.identifier.split('-')[0]).lower()])))

print "Start"
tree=findingRel3.tree
phrases_list=[]
print " Starting"
#phrases_list=phrases_list+list(delve(tree.get_node('married-3'),i_dict[('married')]))
for i in tree.nodes.items():
    print "I    ",i
    if ((i[0].split('-'))[0]).lower() not in wh_list:
        phrases_list=phrases_list+list(delve(i[1],i_dict[(i[0].split('-')[0]).lower()]))

print set(phrases_list)