import rdflib
from rdflib import Graph, URIRef, RDF
from rdflib import Namespace
import nltk.tokenize
import SPARQLWrapper
######################################
#  A quick test of a python library reflib to get data from an rdf graph
# D Moore 15/3/2014
# needs rdflib > version 3.0

# CHANGE THE URI BELOW TO A DIFFERENT PERSON AND SEE WHAT HAPPENS
# COULD DO WITH A WEB FORM
# NOTES:
#
#URI_ref = 'http://dbpedia.org/resource/Richard_Nixon'
#URI_ref = 'http://dbpedia.org/resource/Margaret_Thatcher'
#URI_ref = 'http://dbpedia.org/resource/Isaac_Newton'
#URI_ref = 'http://dbpedia.org/resource/Richard_Nixon'
URI_ref = 'http://dbpedia.org/resource/Napoleon'
#URI_ref = 'http://dbpedia.org/resource/apple'
##########################################################


def get_name_from_uri(dbpedia_uri):
    # pulls the last part of a uri out and removes underscores
    # got to be an easier way but it works
    output_string = ""
    s = dbpedia_uri
    # chop the url into bits devided by the /
    tokens = s.split("/")
    # because the name of our person is in the last section itterate through each token
    # and replace the underscore with a space
    for i in tokens :
        str = ''.join([i])
        output_string = str.replace('_',' ')
    # returns the name of the person without underscores
    return(output_string)

def is_person(uri):
#####  SPARQL way to do this
    uri = URIRef(uri)
    person = URIRef('http://dbpedia.org/ontology/Person')
    g= Graph()
    g.parse(uri)
    resp = g.query(
        "ASK {?uri a ?person}",
        initBindings={'uri': uri, 'person': person}
    )
    print uri, "is a person?", resp.askAnswer
    return resp.askAnswer
def spouse(uri):
    uri = URIRef(uri)
    person = URIRef('http://dbpedia.org/ontology/Person')
    g= Graph()
    g.parse(uri)
    resp = g.query("""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    ,dbpedia:<http://www.dbpedia.org/resources#>,dbpedia-owl:<http://www.dbpedia.org/ontology#>
    select ?spouse ?spouseName where {
                             dbpedia:Napoleon dbpedia-owl:spouse ?spouse .
                             ?spouse rdfs:label ?spouseName .
                             filter( langMatches(lang(?spouseName),"en") )
                             }""")
    return resp.askAnswer
################### this is new , our own query ##################
from SPARQLWrapper import SPARQLWrapper, JSON, N3

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                   PREFIX dbpedia:<http://dbpedia.org/resource>
                   PREFIX dbpedia-this: <http://dbpedia.org/ontology/>
                   select ?spouse ?spouseName where {
                             <http://dbpedia.org/resource/Napoleon> <http://dbpedia.org/ontology/spouse> ?spouse .
                             ?spouse rdfs:label ?spouseName.
                             filter( langMatches(lang(?spouseName),"en") )
                   } limit 5""")   #      ......  .


'''
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
'''
print "spouse:  ----------------------"

'''
#for row in sparql:
#    print("%s knows %s" % row)
print '\n\n*** N3 Example'
sparql.setReturnFormat(N3)
results = sparql.query().convert()
print results
'''
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
#print results
for result in results["results"]["bindings"]:
    #print result["spouse"]["value"],"  ",get_name_from_uri(result["spouse"]["value"])
    print result["spouse"]["value"],"  ",result["spouseName"]["value"]
############### till here #########################

#print spouse(URI_ref)
URI_NAME = get_name_from_uri(URI_ref)
NAME_LABEL = ''

if is_person(URI_ref):
    print "Accessing facts for", URI_NAME, " held at ", URI_ref
'''
    g = Graph()
    g.parse(URI_ref)
    print "Person Extract for", URI_NAME
    print "There are ",len(g)," facts about", URI_NAME, "stored at the URI ",URI_ref
    print "Here are a few:-"


    # Ok so lets get some facts for our person
    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthName")):
        print URI_NAME, "was born " + str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/deathDate")):
        print URI_NAME, "died on", str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")):
        print URI_NAME, "was born on", str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/eyeColor")):
        print URI_NAME, "had eyes coloured", str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/property/spouse")):
        print URI_NAME, "was married to ", get_name_from_uri(str(stmt[1]))

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/reigned")):
        print URI_NAME, "reigned ", get_name_from_uri(str(stmt[1]))

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/children")):
        print URI_NAME, "had a child called ", get_name_from_uri(str(stmt[1]))

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/property/profession")):
        print URI_NAME, "(PROPERTY profession) was trained as a  ", get_name_from_uri(str(stmt[1]))

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/property/child")):
        print URI_NAME, "PROPERTY child ", get_name_from_uri(str(stmt[1]))

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/property/deathplace")):
        print URI_NAME, "(PROPERTY death place) died at: ", str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/property/title")):
        print URI_NAME, "(PROPERTY title) Held the title: ", str(stmt[1])


    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/sex")):
        print URI_NAME, "was a ", str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/knownfor")):
        print URI_NAME, "was known for ", str(stmt[1])

    for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthPlace")):
        print URI_NAME, "was born in ", get_name_from_uri(str(stmt[1]))



else:
    print "ERROR - "
    print "Resource", URI_ref, 'does not look to be a person or there is no record in dbpedia'

'''






{u'head': {u'link': [], u'vars': [u'label']}, u'results': {u'distinct': False, u'bindings': [{u'label': {u'xml:lang': u'en', u'type': u'literal', u'value': u'Asturias'}}, {u'label': {u'xml:lang': u'ar', u'type': u'literal', u'value': u'\u0645\u0646\u0637\u0642\u0629 \u0623\u0633\u062a\u0648\u0631\u064a\u0627\u0633'}}, {u'label': {u'xml:lang': u'de', u'type': u'literal', u'value': u'Asturien'}}, {u'label': {u'xml:lang': u'es', u'type': u'literal', u'value': u'Asturias'}}, {u'label': {u'xml:lang': u'fr', u'type': u'literal', u'value': u'Asturies'}}, {u'label': {u'xml:lang': u'it', u'type': u'literal', u'value': u'Asturie'}}, {u'label': {u'xml:lang': u'ja', u'type': u'literal', u'value': u'\u30a2\u30b9\u30c8\u30a5\u30ea\u30a2\u30b9\u5dde'}}, {u'label': {u'xml:lang': u'nl', u'type': u'literal', u'value': u'Asturi\xeb (regio)'}}, {u'label': {u'xml:lang': u'pl', u'type': u'literal', u'value': u'Asturia'}}, {u'label': {u'xml:lang': u'pt', u'type': u'literal', u'value': u'Ast\xfarias'}}, {u'label': {u'xml:lang': u'ru', u'type': u'literal', u'value': u'\u0410\u0441\u0442\u0443\u0440\u0438\u044f'}}, {u'label': {u'xml:lang': u'zh', u'type': u'literal', u'value': u'\u963f\u65af\u56fe\u91cc\u4e9a\u65af'}}], u'ordered': True}}