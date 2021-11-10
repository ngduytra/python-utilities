from itertools import count
import random
from urllib.request import urlopen
import sys

WORLD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()" : "Set *** to an instance of class %%%.",
    "***.***(@@@)" : "From *** fet the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'" : "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORLD_URL).readlines():
    WORDS.append(word.strip())

def convert(snipet, phrase):
    class_names = [w.decode('utf-8') for w in random.sample(WORDS, snipet.count("%%%"))]
    other_names = [w.decode('utf-8') for w in random.sample(WORDS, snipet.count("***"))]
    results = []
    param_names = []

    for i in range(0, snipet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append('_'.join(x.decode('utf-8') for x in random.sample(WORDS, param_count)))

    for sentence in snipet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snipets = list(PHRASES.keys())
        random.shuffle(snipets)

        for snipet in snipets:
            phrase = PHRASES[snipet]
            question, answer = convert(snipet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

        input("> ")
        print("ANSWER: %s\n\n" % answer)

except EOFError:
    print("\nBye")