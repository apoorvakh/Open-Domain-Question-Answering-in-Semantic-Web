
from nltk import tokenize
#from __future__ import print_function
from alchemyapi import AlchemyAPI
import json



# ########## Getting triples from a given Sentence #########
def get_triples(txt):
    response_spo = alchemyapi.relations('text', txt)

    if response_spo['status'] == 'OK':
        for relation in response_spo['relations']:
            if 'subject' in relation:
                print('Subject: ', relation['subject']['text'].encode('utf-8'))
                spo_dict['subject'] = relation['subject']['text']
            if 'action' in relation:
                print('Action: ', relation['action']['text'].encode('utf-8'))
                spo_dict['predicate']=relation['action']['text']
            if 'object' in relation:
                print('Object: ', relation['object']['text'].encode('utf-8'))
                spo_dict['object']=relation['object']['text']

    else:
        print('Error in relation extaction call: ', response['statusInfo'])



    response = alchemyapi.combined('text', demo_txt)

    if response['status'] == 'OK':
        print('## Response Object ##')
        #print(json.dumps(response, indent=4))

        print('')

        print('## Keywords ##')
        for keyword in response['keywords']:
            print(keyword['text'], ' : ', keyword['relevance'])

    else:
        print('Error in combined call: ', response['statusInfo'])






# ### Getting out different parts of the query sentence
co_ref = open('testing_state_complex.txt','r')
sen_list=[]
for i in co_ref:
    sen_list.append(i.split('"')[1])

#print sen_list

# Get triples for each sentence and ///////////////////////////
for s in sen_list:
    print "############################"
    l=get_triples(s)
    print "\n\n\n"


