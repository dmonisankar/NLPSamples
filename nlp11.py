# Creating and querying a corpus with gensim


# It's time to apply the methods you learned in the previous video to create your first gensim dictionary and corpus!

# You'll use these data structures to investigate word trends and potential interesting topics in your document set. To get started, we have imported a few additional messy articles from Wikipedia, which were preprocessed by lowercasing all words, tokenizing them, and removing stop words and punctuation. These were then stored in a list of document tokens called articles. You'll need to do some light preprocessing and then generate the gensim dictionary and corpus.


# Import Dictionary
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize

my_documents = ['The movie was about a spaceship and aliens.', 'I really liked the movie!', 'Awesome action scenes, but boring characters.', 'The movie was awful! I hate alien films.', 'Space is cool! I liked the movie.', 'More space films, please!', 'The movies has been made by latest computer technology', 'Advanment in computer technology has changed the quality of movies']

articles = [word_tokenize(doc.lower()) for doc in my_documents]

for article in articles:
	print(article)

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)


# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(articles[4])
print(corpus[4][:10])
print(dictionary.token2id.get("space"))
print(dictionary.get(0))
