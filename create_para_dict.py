import pickle
### method to create a paraphrase dictionary ###
from collections import defaultdict

f_freebase = open('F:\\ABCD\\PESIT\\adaM\\Summer2015\\DataSet\\datasets\\patty-dataset-freebase\\dbpedia-relation-paraphrases.txt','r')
f_yago = open('F:\\ABCD\\PESIT\\adaM\\Summer2015\\DataSet\\datasets\\patty-dataset-freebase\\yago-relation-paraphrases.txt','r')
para_dict = defaultdict(set)

def removeBrac(txt):
    splitted=txt.split()
    #print "splitted  ",splitted
    line=""
    for i in splitted:
        if not (i.startswith('[[')):
            line=line+" "+ i
            #print line
    return line


def create_para_dict(file_f,file_y):
    #para_dict = defaultdict(list)
    for i in file_f:
        j = i.split('\t') #splitting at the tab
        '''if removeBrac(j[1][:-1]).strip()=="":
            print j[1]
        else:'''
        para_dict[removeBrac(j[1][:-2]).strip()].add(j[0].strip())
        #print para_dict[removeBrac(j[1][:-2])] # the RHS will be the key.
    for i in file_y:
        j = i.split('\t') #splitting at the tab
        '''if removeBrac(j[1][:-1]).strip()=="":
            print j[1]
        else:'''
        para_dict[removeBrac(j[1][:-2]).strip()].add(j[0].strip())
    return para_dict

para_dict = create_para_dict(f_freebase,f_yago)
#pickle.dump(para_dict,open('para_dict.p','w'))

f_freebase.close()
f_yago.close()







