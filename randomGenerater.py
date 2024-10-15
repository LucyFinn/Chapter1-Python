import random
emptyList = []

# article noun verb atricle noun preposition verb
articles = ["the", "a", "one", "some", "any"]
nouns = ["teacher", "student", "principal", "library", "school"]
verbs = ["taught", "learned", "read", "walked", "ran"]
prepositions = ["to", "from", "over", "under", "on"]

article1 = random.choice(articles)
noun1 = random.choice(nouns)
verb1 = random.choice(verbs)
article2 = random.choice(articles)
noun2 = random.choice(nouns)
prep = random.choice(prepositions)
verb2 = random.choice(verbs)

emptyList.append(article1)
emptyList.append(noun1)
emptyList.append(verb1)
emptyList.append(article2)
emptyList.append(noun2)
emptyList.append(prep)
emptyList.append(verb2)

print(emptyList)
