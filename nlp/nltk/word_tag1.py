import nltk

line = 'i love this world which was beloved by all the people here'
tokens = nltk.word_tokenize(line)
# ['i', 'love', 'this', 'world', 'which', 'was', 'beloved', 'by',
# 'all', 'the', 'people', 'here']
pos_tags = nltk.pos_tag(tokens)
# [('i', 'RB'), ('love', 'VBP'), ('this', 'DT'), ('world', 'NN'), ('which', 'WDT'),
# ('was', 'VBD'), ('beloved', 'VBN'), ('by', 'IN'), ('all', 'PDT'), ('the', 'DT'),
# ('people', 'NNS'), ('here', 'RB')]
for word, pos in pos_tags:
    if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
        print(word, pos)
# world NN
# people NNS
