from polyglot.text import Text

article = """El presidente de la Generalitat de Cataluña, Carles Puigdemont, ha afirmado hoy a la alcaldesa de Madrid, Manuela Carmena, que en su etapa de alcalde de Girona (de julio de 2011 a enero de 2016) hizo una gran promoción de Madrid."""

# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of each entity
print(type(ent))