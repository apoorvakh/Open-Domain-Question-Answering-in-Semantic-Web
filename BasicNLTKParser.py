#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Apoorva
#
# Created:     15/06/2015
# Copyright:   (c) Apoorva 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from nltk import tokenize
para = "Hello. My name is Jacob. Which book is written by Orhan Pamuk. The President of United States of America"
sents = tokenize.sent_tokenize(para)
sents

sent = tokenize.word_tokenize(sents[2])
print "Sentence",sent

from nltk import tag
tagged_sent = tag.pos_tag(sent)
tagged_sent

from nltk import chunk
tree = chunk.ne_chunk(tagged_sent)
print tree
tree.draw()

print "display"
#tree.display()

print "\n\n\n-----------New try---------------\n"

import nltk
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)
result.draw()

print "\n\n\n--------------------New Try---------------------\n"

from nltk.tree import *
from nltk.draw import tree
print Tree(1, [2, 3, 4])
s = Tree('S', [Tree('NP', ['I']),
           Tree('VP', [Tree('V', ['saw']),
               Tree('NP', ['him'])])])
print s
dp1 = Tree('dp', [Tree('d', ['the']), Tree('np', ['dog'])])
dp2 = Tree('dp', [Tree('d', ['the']), Tree('np', ['cat'])])
vp = Tree('vp', [Tree('v', ['chased']), dp2])
sentence = Tree('s', [dp1, vp])
print sentence
sentence.draw()



