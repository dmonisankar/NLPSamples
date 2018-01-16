import spacy


nlp = spacy.load('en')
print(nlp.entity)

doc = nlp("""Berlin is the capital of Germany; and the residence of Chancellor Angela Merkel.""")
print(doc.ents)

for ent in doc.ents:
	print(ent, ent.label_)
