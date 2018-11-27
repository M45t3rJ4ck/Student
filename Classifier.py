# === Your task ===
# If you understand the above - well done! It's something that definitely isn't done at UKZN until honors.
# Yet it isn't that complicated because Python has tools like NLTK to help you
# Now, make sure all the code in this Task of using NLTK works for you and is in your file classifier.py
# At the bottom of classifier.py, using your classifier, classify the following tweets:
# "My house is not great"
# "The movie is not bad"
# "your song is annoying"
# See any problems? Can you suggest why these problems arise in these SPECIFIC tweets?


import nltk

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]
neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]
tweets = []

for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


all_words = get_words_in_tweets(tweets)
word_features = get_word_features(all_words)


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


tweet1 = "My house is not great"
tweet2 = "The movie is not bad"
tweet3 = "your song is annoying"
tweet4 = "Riaz is not my friend"

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
tweet1Split = tweet1.split()
tweet1SplitAndExtract = extract_features(tweet1Split)
print(classifier.classify(tweet1SplitAndExtract))
tweet2Split = tweet2.split()
tweet2SplitAndExtract = extract_features(tweet2Split)
print(classifier.classify(tweet2SplitAndExtract))
tweet3Split = tweet3.split()
tweet3SplitAndExtract = extract_features(tweet3Split)
print(classifier.classify(tweet3SplitAndExtract))
tweet4Split = tweet4.split()
tweet4SplitAndExtract = extract_features(tweet4Split)
print(classifier.classify(tweet4SplitAndExtract))


# To us as humans "not bad" is a sign of something being okay, not great, but just okay...in the setup of our
# classifier, we determined that "not" & "bad" is negative words and therefor it has been classified as negative.
# Whereas annoying was not classified at all yet.
