from fuzzywuzzy import fuzz
import nltk
from nltk import tokenize,pos_tag

java_file = open('java_op.txt','r')

max_ratio=0
subject =""

for i in java_file:
    temp_list_of_pos=tokenize.wordpunct_tokenize(i)
    x= (fuzz.ratio("subj",temp_list_of_pos[:1]))
    if x>max_ratio :
        max_ratio=x
        subject= temp_list_of_pos[len(temp_list_of_pos)-4]

print subject



