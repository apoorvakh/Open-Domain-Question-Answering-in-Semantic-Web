from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import pickle

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

demo_txt = "Where did the president of USA study?"

print('Processing text: ', demo_txt)
print('')

response = alchemyapi.relations('text', demo_txt)
spo_dict = {}

if response['status'] == 'OK':
    #print('## Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Relations ##')
    for relation in response['relations']:
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


pickle.dump(spo_dict,open('spo_dict.p','wb'))


print('Processing text: ', demo_txt)
print('')

response = alchemyapi.combined('text', demo_txt)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')

    print('## Keywords ##')
    for keyword in response['keywords']:
        print(keyword['text'], ' : ', keyword['relevance'])
    print('')

    print('## Concepts ##')
    for concept in response['concepts']:
        print(concept['text'], ' : ', concept['relevance'])
    print('')

    print('## Entities ##')
    for entity in response['entities']:
        print(entity['type'], ' : ', entity['text'], ', ', entity['relevance'])
    print(' ')

else:
    print('Error in combined call: ', response['statusInfo'])

print('')
print('')
