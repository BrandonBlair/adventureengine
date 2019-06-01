import nltk
import yaml


def load_map():
    map_file = open('map.yml', 'r')
    game_map = yaml.load(map_file, Loader=yaml.Loader)
    return game_map


def parse_user_input(command):
    tokenized = nltk.word_tokenize(command)
    tokens = nltk.pos_tag(tokenized, tagset='universal')
    print(tokens)

    words = {
        'verbs': [],
        'adjectives': [],
        'predicates': [],
        'determiners': [],
        'adverbs': [],
        'nouns': []
    }

    for tok in tokens:
        if tok[1] == 'VERB':
            words['verbs'].append(tok[0])
        elif tok[1] == 'ADP':
            words['predicates'].append(tok[0])
        elif tok[1] == 'DET':
            words['determiners'].append(tok[0])
        elif tok[1] == 'ADJ':
            words['adjectives'].append(tok[0])
        elif tok[1].startswith('NOUN'):
            words['nouns'].append(tok[0])

    return words
