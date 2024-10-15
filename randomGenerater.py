import random
emptyList = []

# article noun verb atricle noun preposition verb
articles = ["the", "a", "one", "some", "any"]
nouns = ["teacher", "student", "principal", "library", "school"]
verbs = ["taught", "learned", "read", "walked", "ran"]
prepositions = ["to", "from", "over", "under", "on"]

firstWord = random.choice(articles)

emptyList.append(firstWord)
print(emptyList)
