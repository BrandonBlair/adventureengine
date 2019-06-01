import sys

from resources.utils import load_map, parse_user_input

USER_START_TILE = 'A01'

game_map = load_map()
current_tile = game_map.tiles[USER_START_TILE]

try:
    while True:
        print(game_map.describe_location(current_tile))
        user_input = input()
        sentence = parse_user_input(user_input)
        print(sentence)
        if 'go' in sentence['verbs'] and sentence['nouns'][-1] in game_map.tiles:
            current_tile = game_map.tiles[sentence['nouns'][-1]]
except KeyboardInterrupt as e:
    sys.exit(0)

