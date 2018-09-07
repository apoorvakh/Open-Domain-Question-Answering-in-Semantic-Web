f = open('C:\\Users\\Apoorva\\Desktop\\ABCD\\PESIT\\adaM\\Summer2015\\DataSet\\datasets\\patty-dataset\\patty-dataset\\wikipedia-patterns.txt','r')

wiki_dict = {}

f.readline()

for i in f:
    t = i.replace('\t','""').replace(';$','""').split('""')
    if '' in t:
       t = filter(lambda name: name.strip(), t)
    #print t
    """
       pattern id
       patterntext
       confidence
       domain
       range
    """
    #print i
    domain = t[-2].split('_')
    d = domain[0] + " "+domain[1]
    range = t[-1].split('_')
    r = range[0] +" "+ range[1]
    wiki_dict[t[0]] = {'pattern_text':[i for i in t[1:-3] if i!=''],'confidence':t[-3],'domain':d,'range':r}

f.close()
