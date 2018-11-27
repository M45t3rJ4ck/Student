# ======================= 		Learning how to use NLTK - Task 2    ============================#
# 	Create a new python file in this folder called gardenpath.py
# 	In the file type the following code:
import nltk

sentence = "I made her duck"
tokens = nltk.word_tokenize(sentence)
print(nltk.pos_tag(tokens))
print("Tagset for NLTK \n")
print(nltk.help.upenn_tagset('PRP'))
print(nltk.help.upenn_tagset('VBD'))
print(nltk.help.upenn_tagset('NN'))
print(nltk.help.upenn_tagset('VBP'))

# === Your task ===
#   Let's have some 'fun'.
#   Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read at what a 'Garden Path sentence' is
#   (at the top) and look at the 'Examples'. Remember that 'parsing' is when we or a computer try tag words given to us
#   to so we can understand what the sentence actually MEANS. Use some Garden Path sentences or think up your own (at
#   least 5). In your file called garden.py that should be working in for this task, tokenize and pos tag each of the
#   sentences after you have stored them in a list called garden path Sentences. See how NLTK has pos tagged these
#   sentences and look up the POS tags you don't understand by using the nltk.help.upenn_tag set command. At the bottom
#   of your file, write a comment about one unusual tag you found that NLTK gave one of the words of your sentences -
#   did you expect this?
garden_path = ["Until the police arrest the drug dealers control the street.",
               "The prime number few.",
               "The man who hunts ducks out on weekends.",
               "The cotton clothing is usually made of grows in Mississippi.",
               "That Jill is never here hurts.",
               "We painted the wall with cracks."]
for sentence in garden_path:
    list_words = sentence.split()
    tokens = nltk.word_tokenize(sentence)
    print(nltk.pos_tag(tokens))
print("\n")
print("\nGarden Path Tagset\n")
print(nltk.help.upenn_tagset('IN'))
print(nltk.help.upenn_tagset('DT'))
print(nltk.help.upenn_tagset('NNS'))
print(nltk.help.upenn_tagset('JJ'))
print(nltk.help.upenn_tagset('WP'))
print(nltk.help.upenn_tagset('VBZ'))
print(nltk.help.upenn_tagset('RB'))
