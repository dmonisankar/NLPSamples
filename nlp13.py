# Tf-idf with Wikipedia

# Now it's your turn to determine new significant terms for your corpus by applying gensim's tf-idf. You will again have access to the same corpus and dictionary objects you created in the previous exercises - dictionary, corpus, and doc. Will tf-idf make for more interesting results on the document level?

# Import Dictionary
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize


# Import TfidfModel
from gensim.models.tfidfmodel import TfidfModel

my_documents = ['The movie was about a spaceship and aliens.', 'I really liked the movie!', 'Awesome action scenes, but boring characters.', 'The movie was awful! I hate alien films.', 'Space is cool! I liked the movie.', 'More space films, please!', 'The movies has been made by latest computer technology', 'Advanment in computer technology has changed the quality of movies']

articles = [word_tokenize(doc.lower()) for doc in my_documents]

# for article in articles:
	# print(article)

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)


# # Select the id for "computer": computer_id
# computer_id = dictionary.token2id.get("computer")

# # Use computer_id with the dictionary to print the word
# print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

for item in corpus:
	print(item)



# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

doc = corpus[0]

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)