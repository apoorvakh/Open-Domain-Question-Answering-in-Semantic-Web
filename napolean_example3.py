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
from SPARQLWrapper import SPARQLWrapper, JSON, N3, XML, RDF

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                   PREFIX dbpedia:<http://dbpedia.org/resource>
                   PREFIX dbpedia-this: <http://dbpedia.org/ontology/>
                   select ?spouse ?spouseName where {
                             <http://dbpedia.org/resource/Napoleon> <http://dbpedia.org/ontology/spouse> ?spouse .
                             ?spouse rdfs:label ?spouseName.
                             filter( langMatches(lang(?spouseName),"en") )
                   } limit 5""")   #filter( langMatches(lang(?spouseName),"en") )       ...... ?spouse rdfs:label ?spouseName .



print "spouse:  ----------------------"

print " Output w/o format "
res = sparql.query()


print '\n\n*** N3 Example'
sparql.setReturnFormat(N3)
results = sparql.query().convert()
print results

print '\n\n*** JSON Example'
sparql.setReturnFormat(JSON)
res = sparql.query()
print res.print_results()
results = sparql.query().convert()
#print results
print "\nby using variables explicitly"
for result in results["results"]["bindings"]:
    print result["spouse"]["value"],"  ",result["spouseName"]["value"]

print '\n\n*** XML Example'
sparql.setReturnFormat(XML)
results = sparql.query().convert()
print results.toxml()




############### till here #########################

#print spouse(URI_ref)
URI_NAME = get_name_from_uri(URI_ref)
NAME_LABEL = ''
'''
if is_person(URI_ref):
    print "Accessing facts for", URI_NAME, " held at ", URI_ref

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

{u'head': {u'link': [], u'vars': [u'spouse', u'spouseName']}, u'results': {u'distinct': False, u'bindings': [{u'spouse': {u'type': u'uri', u'value': u'http://dbpedia.org/resource/Jos%C3%A9phine_de_Beauharnais'}, u'spouseName': {u'xml:lang': u'en', u'type': u'literal', u'value': u'Jos\xe9phine de Beauharnais'}}, {u'spouse': {u'type': u'uri', u'value': u'http://dbpedia.org/resource/Marie_Louise,_Duchess_of_Parma'}, u'spouseName': {u'xml:lang': u'en', u'type': u'literal', u'value': u'Marie Louise, Duchess of Parma'}}], u'ordered': True}}