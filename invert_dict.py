import pickle
from collections import defaultdict

para_dict = pickle.load(open('para_dict.p','r'))
print "main len",len(para_dict.keys())
invert_para_dict = defaultdict(list)

k=0
for i in para_dict.keys():
    temp_list = para_dict[i] #[actedIn,created,directed...]
    for j in temp_list:
        invert_para_dict[j].append(i)
        k=k+1 #to count the number of items we are going to have

print "inverted len    ",len(invert_para_dict.keys())



