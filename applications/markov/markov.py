import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
next_word = {'start_words':[], 'end_words':[]}

def gen_lookup_table():
    # split input string to array
    words_collection = words.split()
    # compile words than can be followed by 
    for i in range(len(words_collection)-1):
        word = words_collection[i]
        word_fol = words_collection[i+1]

        if word not in next_word:
            next_word[word] = [word_fol]
        else:
            next_word[word].append(word_fol)
        if word[0].isupper() or (word[0] == '"' and word[1].isupper()):
            next_word['start_words'].append(word)
        end_check = '. ? ! ." ?" !"'.split()
        for i,ele in enumerate(end_check):
            if i <= 2 and word[-1] == ele:
                next_word['end_words'].append(word)
            elif i > 2 and word[-2:] == ele:
                next_word['end_words'].append(word)

gen_lookup_table()

# TODO: construct 5 random sentences
# Your code here
def gobbledegook(sentence_count):
    i = 1
    res = [None]
    while i <= sentence_count:
        sentence = ""
        word_list = []
        word_list.append(random.choice(next_word['start_words']))

        next = random.choice(next_word[word_list[len(word_list)-1]])
        while next not in next_word['end_words']:
            word_list.append(next)
            next = random.choice(next_word[word_list[len(word_list)-1]])
        word_list.append(next)
        for s in word_list:
            print(s, end=" ")
        print("")
        i += 1

gobbledegook(5)