from rdflib import Graph
from rdflib import URIRef
import rdflib
import pprint
from rdflib.namespace import RDF
from rdflib.namespace import OWL
from ontospy import ontospy


obj = ontospy.Ontology('http://dbpedia.org/ontology/')
g = Graph()
g.load('http://dbpedia.org/resource/')
'''for i in obj.allclasses:
    print i
g = Graph()

g.parse('disambiguations_en_try_sample.nt',format='nt')
#print len(g)
Alien = URIRef('http://dbpedia.org/resource/Alien')
#subj=rdflib.URIRef()
y = g.triples(Alien)

#for i in y:
    #print str(i)
    #print "hi"
    '''
'''for i in y:
    if(Alien, RDF.type, OWL.sameAs ) in str(i):
              print "This graph knows that Bob is a person!"
              '''








