#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Aarti
#
# Created:     15/06/2015
# Copyright:   (c) Aarti 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import nltk
#from nltk.parse import stanford as st
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import os
java_path = 'C:\\Program Files\\Java\\jdk1.8.0_05\\bin\\java.exe'
os.environ['JAVAHOME'] = java_path
def main():
    pass

if __name__ == '__main__':
    main()
    '''
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,corpus='ieer', pattern = IN):
        print rel
'''
#print nltk.corpus.treebank.tagged_sents()[20]
s=nltk.word_tokenize('Who is the wife of the President of the United States of America?')
sent =nltk.pos_tag(s)# nltk.corpus.treebank.tagged_sents()[20]
#print sent

#print nltk.ne_chunk(sent, binary=True)
#parser = st.StanfordParser()







import os
from nltk.parse import stanford


os.environ['STANFORD_PARSER'] = 'C:\\Users\\Apoorva\\Desktop\\ABCD\\PESIT\\adaM\\Summer2015\\jars\\stanford-parser.jar'
os.environ['STANFORD_MODELS'] = 'C:\\Users\\Apoorva\\Desktop\\ABCD\\PESIT\\adaM\\Summer2015\\jars\\stanford-parser-3.5.2-models.jar'
#os.environ['JAVAHOME'] = 'c:/Program Files/java/jre7/bin'

java_path = "C:/Program Files/Java/jdk1.8.0_20/bin/java.exe"
os.environ['JAVAHOME'] = java_path


#parser = stanford.StanfordParser(model_path="C:\Users\Apoorva\Desktop\ABCD\PESIT\adaM\Summer2015\jars\stanford-parser-3.5.2-models\edu\stanford\nlp\models\lexparser\englishPCFG.ser.gz")
parser = stanford.StanfordParser(model_path='englishPCFG.ser.gz')


#os.environ['STANFORD_PARSER'] = 'stanford-parser-full-2015-04-20\\stanford-parser-full-2015-04-20\\stanford-parser.jar'
#os.environ['STANFORD_MODELS'] = 'stanford-parser-full-2015-04-20\\stanford-parser-full-2015-04-20\\stanford-parser-3.5.2-models.jar'


#parser = stanford.StanfordParser(model_path='englishPCFG.ser.gz')
#sentences = parser.raw_parse_sents(("Hello, My name is Aarti.", "What is your name?","The President of United States of America","who is the wife of actor of Harry Potter?"))
#print sentences
sentences1 = parser.raw_parse("Who is the wife of the actor who starred in Harry Potter?")
#print list(sentences1)
#for line in sentences1:
    #print type(line)
dependencies = parser.parseToStanfordDependencies('Pick up the tire pallet')
tupleResult = [(rel, gov.text, dep.text) for rel, gov, dep in dependencies.dependencies]

# GUI
for line in sentences1:
    for sentence in line:
        sentence.draw()