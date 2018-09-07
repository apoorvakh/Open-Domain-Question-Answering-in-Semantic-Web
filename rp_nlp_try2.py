from treelib import Tree,Node
import pickle
import findingRel3
from sqlitedict import SqliteDict
wh_list=['who','what','where','which','whom']
#print "Opening"
#i_dict=pickle.load(open('inverted_index.p'))
i_dict=SqliteDict("my_db.sqlite",autocommit=True)
#print " opened"

def delve(node,inverted_list):
    #print type(node)
    print "Node ",node.identifier
    #gives the node list of all the children
    n_list=tree.children(node.identifier)#.split('-')[0])

    #print "n_list    :",n_list
    id_list=[]
    remove_list=[]
    if len(n_list)!=0: #added now
        for i in n_list:
            if ((i.identifier.split('-'))[0]).lower() not in wh_list:
                id_list.append((i.identifier.split('-')[0]).lower().strip())
            else:
                remove_list.append(i)
        for x in remove_list:
            n_list.remove(x)
    #print "id_list ",id_list
    intersect=inverted_list

    if len(id_list)!=0:
        for c in id_list:#each child of w
            #print"C : ",c

            if c in i_dict.keys():
                #print" In : C : ",c
                if len(list(set(intersect).intersection(set(i_dict[c]))))==0:
                    #return intersect
                    continue

                elif len(list(set(intersect).intersection(set(i_dict[c]))))>0:
                    intersect=list(set(intersect).intersection(set(i_dict[c])))
                    #print "inter    : ",intersect
                    intersect=delve(n_list[id_list.index(c)],intersect)

        return intersect

                    #return intersect #added now
            #else:
    else:
        #print "GIVING ERROR!"
        #return list(set(inverted_list).intersection(set(i_dict[(node.identifier.split('-')[0].strip()).lower()])))
        return inverted_list

#print "Start"
tree=findingRel3.tree
phrases_list=[]
print " Starting"
#phrases_list=phrases_list+list(delve(tree.get_node('married-3'),i_dict[('married')]))
for i in tree.nodes.items():
    #print "I    ",i
    if ((i[0].split('-'))[0]).lower() not in wh_list:
        a = (i[0].split('-')[0]).lower().strip()
        if a in i_dict.keys():
           #print "TYPE     ",type(delve(i[1],i_dict[a])),"#####"
           #print "phrase list    ",phrases_list
           l= delve(i[1],i_dict[a])
           print "L L L length",len(l)
           if len(l)<5:
                print " L L L : ",l
           #phrases_list=phrases_list+(list(delve(i[1],i_dict[a])))

#print set(phrases_list)
