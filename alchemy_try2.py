from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import pickle
from fuzzywuzzy import fuzz

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()
final_list = pickle.load(open('final_sub_queries.p','rb'))

#for reference, we create the spo_file
spo_file = open('spo.txt','wb')
#for pickling and reusing purpose:
spo_dict = {}
'''
for i in reversed(final_list):
    response = alchemyapi.relations('text', demo_txt)
    if response['status'] == 'OK':
       for relation in response['relations']:
        if 'subject' in relation:
            spo_file.write(relation['subject']['text'].encode('utf-8'))
            #print('Subject: ', relation['subject']['text'].encode('utf-8'))
            spo_dict['subject'] = relation['subject']['text']
        if 'action' in relation:
            spo_file.write(['action']['text'].encode('utf-8'))
            #print('Action: ', relation['action']['text'].encode('utf-8'))
            spo_dict['predicate']=relation['action']['text']
        if 'object' in relation:
            spo_file.write(relation['object']['text'].encode('utf-8'))
            #print('Object: ', relation['object']['text'].encode('utf-8'))
            spo_dict['object']=relation['object']['text']


'''










demo_txt = 'the actor who acted in Harry Potter'

print('Processing text: ', demo_txt)
print('')

response_spo = alchemyapi.relations('text', demo_txt)


if response_spo['status'] == 'OK':
    #print('## Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Relations ##')
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

        print('')
else:
    print('Error in relation extaction call: ', response['statusInfo'])

acceptable_source_uri = [u'dbpedia',u'freebase',u'yago']














print('Processing text: ', demo_txt)
print('')

response = alchemyapi.combined('text', demo_txt)

if response['status'] == 'OK':
    print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')

    print('## Keywords ##')
    for keyword in response['keywords']:
        print(keyword['text'], ' : ', keyword['relevance'])
    print('')
##############required!!!#####################
    print('## Concepts ##')
    #for concept in response['concepts']:
        #print(concept['text'], ' : ', concept['relevance'])
    #print('')

    print('## Entities ##')
    #for entity in response['entities']:
        #print(entity['type'], ' : ', entity['text'], ', ', entity['relevance'])
    print(' ')

else:
    print('Error in combined call: ', response['statusInfo'])
#print('')
#print('')





############## SEE FROM HERE #################################
#max_rel takes care of disambiguation here,many dictionaries are created coz of diff meanings. we take only the one which is relevant to us
# fuzzy match is done coz always we might not get the same o/p for object and
for i in response['concepts']:
    max_rel = 0
    if(set(acceptable_source_uri).issubset(i.keys()) and (fuzz.ratio(i['text'],spo_dict['object']) > 0.5 or fuzz.ratio(i['text'],spo_dict['subject'])>0.5)  and i['relevance'] > max_rel):
                #noting which of subject or object is matched
                if fuzz.ratio(i['text'],spo_dict['object']) > 0.5:
                   spo_dict['s_p_o'] = 'o'
                else:
                   spo_dict['s_p_o'] = 's'
                #print("enterded!!!!!!!!!!!!!")
                if i['relevance'] > max_rel:
                   max_rel = i['relevance']
                if 'dbpedia' in i.keys():
                  spo_dict['which_uri'] = 'dbpedia'
                  spo_dict['uri'] = i['dbpedia']
                  #print ("inside db")
                  break
                if 'freebase' in i.keys():
                  spo_dict['which_uri'] = 'freebase'
                  spo_dict['uri'] = i['freebase']
                  break
                if 'yago' in i.keys():
                  spo_dict['which_uri'] = 'yago'
                  spo_dict['uri'] = i['yago']
                  break


pickle.dump(spo_dict,open('spo_dict.p','wb'))