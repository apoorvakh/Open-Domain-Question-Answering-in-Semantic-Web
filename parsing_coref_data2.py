from nltk import tokenize



co_ref = open('testing_state_complex.txt','r')
li=[]
final_list=[]
for i in co_ref:
    final_list.append(i.split('"')[1])

print final_list



'''
final_list = []
for j,i in enumerate(li):
    print j,"    ",i
    tok = i.split('"')
    #print"tok","  ",len(tok)
    if len(tok)>2:
       final_list.append(tok[1])

print "\nAnd the final list of sub-queries is.....:"
for i in reversed(final_list):
    print i
    '''