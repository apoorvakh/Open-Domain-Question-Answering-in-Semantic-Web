#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Apoorva
#
# Created:     16/06/2015
# Copyright:   (c) Apoorva 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = 'C:\\Users\\Apoorva\\Desktop\\ABCD\\PESIT\\adaM\\Summer2015\\jars\\stanford-parser.jar'
os.environ['STANFORD_MODELS'] = 'C:\\Users\\Apoorva\\Desktop\\ABCD\\PESIT\\adaM\\Summer2015\\jars\\stanford-parser-3.5.2-models.jar'
#os.environ['JAVAHOME'] = 'c:/Program Files/java/jre7/bin'
#os.environ['JAVAHOME'] = 'C:\\Program Files\\Java\\jre7\\bin'

java_path = "C:/Program Files/Java/jdk1.8.0_20/bin/java.exe"
os.environ['JAVAHOME'] = java_path

#parser = stanford.StanfordParser(model_path="C:\Users\Apoorva\Desktop\ABCD\PESIT\adaM\Summer2015\jars\stanford-parser-3.5.2-models\edu\stanford\nlp\models\lexparser\englishPCFG.ser.gz")
parser = stanford.StanfordParser(model_path='englishPCFG.ser.gz')
print type(parser)
#sentences = parser.raw_parse_sents(("Hello, My name is Apoorva", "What is your name?",'Which book is written by Orhan Pamuk',"The President of United States of America","who is the wife of actor of Harry Potter?","ABC cites the fact that chemical additives are banned in many countries and feels they may be banned in this state too"))
#sentences = parser.raw_parse_sents(("Hello, How are you?",'Which book is written by Orhan Pamuk',"The strongest rain ever recorded in India shut down the financial hub of Mumbai, snapped communication lines, closed airports and forced thousands of people to sleep in their offices or walk home during the night, officials said today."))

ss=('For which newspaper does Krugman write and at which university does he teach and which person critizised him in his op-ed column?')
sentences = parser.raw_parse_sents(ss)
print sentences

# GUI

for line in sentences:
    for sentence in line:
        sentence.draw()
        print sentence





