import nltk
import yaml


def load_map():
    map_file = open('map.yml', 'r')
    game_map = yaml.load(map_file, Loader=yaml.Loader)
    return game_map


def parse_user_input(command):
    tokenized = nltk.word_tokenize(command)
    tokens = nltk.pos_tag(tokenized, tagset='universal')

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


def validate_cmd_verb(verb):
    verb_n = normalize(verb)
    if verb_n != 'go':
        raise UnknownActionError(f'{verb_n} is not a known command')
    return None


def get_move_dest(adjectives, nouns, room_exits):
    adjs = [normalize(adj) for adj in adjectives]
    noun = normalize(nouns[-1])
    dest_n = f"{' '.join(adjs)} {noun}"
    short_descs = set()
    name_tile_map = {}
    for ex in room_exits:
        short_desc = ex.item.short_desc
        short_descs.add(short_desc)
        name_tile_map[short_desc] = ex.tile

    for sd in short_descs:
        sd_set = set(sd.split(' '))

        #If adj/noun pairs don't match, try to match noun only
        if set([dest_n]).issubset(sd_set) or noun in sd_set:
            return name_tile_map[sd]

        raise UnknownDestinationError(f'{dest_n} is not a known destination')



def normalize(txt):
    normal = txt.lower()
    return normal


class UnknownActionError(ValueError):
    pass


class UnknownDestinationError(ValueError):
    pass

