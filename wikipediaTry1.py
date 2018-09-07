import wikipedia as wk


# Check if the provided answer hinders the ambivalent thought of the user
# If not, loop through the other probable entity matches(entities)

entities=wk.search('Obama')

page=wk.page(entities[0])

url=page.url

print "\n\nEntities :\n",entities
print "\nSelected uri : ",url

