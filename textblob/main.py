from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB, Synset

# Create a TextBlob object and print part-of-speech tags
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.tags)  # Prints POS tags
print(wiki.noun_phrases)  # Prints noun phrases

# Sentiment analysis
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(testimonial.sentiment)  # Prints sentiment as polarity and subjectivity
print(testimonial.sentiment.polarity)  # Prints only polarity score

# Working with sentences and words in a TextBlob object
zen = TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
print(zen.words)  # Prints words in the blob
print(zen.sentences)  # Prints sentences in the blob

# Loop through sentences and print sentiment for each
for sentence in zen.sentences:
    print(sentence.sentiment)

# Singularize and pluralize words
sentence = TextBlob("Use 4 spaces per indentation level.")
print(sentence.words)  # Prints words in the sentence
print(sentence.words[2].singularize())  # Singularize the word at index 2
print(sentence.words[-1].pluralize())  # Pluralize the last word

# Lemmatization
w = Word("octopi")
print(w.lemmatize())  # Lemmatize the word "octopi" to its base form

w = Word("parties")
print(w.lemmatize("v"))  # Lemmatize "parties" as a verb

# Finding synonyms using WordNet
word = Word("octopus")
print(word.synsets)  # Prints synsets (meanings) of "octopus"
print(Word("hack").get_synsets(pos=VERB))  # Prints synsets of "hack" as a verb

# Finding path similarity between two words
octopus = Synset('octopus.n.02')
shrimp = Synset('shrimp.n.03')
print(octopus.path_similarity(shrimp))  # Prints similarity score between octopus and shrimp

# Pluralizing words in a TextBlob
animals = TextBlob("cat dog octopus")
print(animals.words.pluralize())  # Pluralizes all the words

# Correcting spelling errors
b = TextBlob("I havv goood speling!")
print(b.correct())  # Prints the corrected sentence

# Spellcheck
w = Word('falibility')
print(w.spellcheck())  # Prints possible correct spellings and their confidence scores

# Counting words in a sentence
monty = TextBlob("We are no longer the Knights who say Ni. We are now the Knights who say Ekki ekki ekki PTANG.")
print(monty.word_counts['ekki'])  # Counts occurrences of 'ekki' in the text
print(monty.words.count('ekki', case_sensitive=True))  # Counts case-sensitive occurrences of 'ekki'

# Parsing a sentence (grammar structure)
b = TextBlob("And now for something completely different.")
print(b.parse())  # Prints the parsed structure of the sentence

# String slicing and finding
var = zen[0:19]  # Slices the first 19 characters from zen
zen.upper()  # Converts all text in zen to uppercase
zen.find("Simple")  # Finds the index of the word "Simple" in zen

# Comparing two TextBlob objects
apple_blob = TextBlob("apples")
banana_blob = TextBlob("bananas")
print(apple_blob < banana_blob)  # Compares two blobs
print(apple_blob == 'apples')  # Checks if the blob is equal to the string 'apples'
print(apple_blob + ' and ' + banana_blob)  # Concatenates two blobs
print("{0} and {1}".format(apple_blob, banana_blob))  # Formats a string using blobs

# Generating n-grams (sequence of n words)
blob = TextBlob("Now is better than never.")
print(blob.ngrams(n=3))  # Prints trigrams (sequences of 3 words)

# Accessing sentence indices
for s in zen.sentences:
    print(s)
    print("---- Starts at index {}, Ends at index {}".format(s.start, s.end))  # Prints start and end index of each sentence
