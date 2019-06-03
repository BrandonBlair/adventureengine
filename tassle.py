import sys

from resources.utils import *
from character import Character

USER_START_TILE = 'A01'

game_map = load_map()
current_tile = game_map.tiles[USER_START_TILE]
char = Character()
try:
    while True:
        print("\n\n")
        print(current_tile.name)
        print("\n")
        print(game_map.loc_desc(current_tile))
        print("\n")
        print("> ", end='')
        user_input = input()
        sentence = parse_user_input(user_input)
        usr_cmd = sentence['verbs'][0]
        try:
            validate_cmd_verb(usr_cmd)
        except UnknownActionError as uae:
            print(f"What do you mean by '{usr_cmd}'?")
            continue

        if usr_cmd == 'go':
            try:
                dest_tile = get_move_dest(sentence['adjectives'], sentence['nouns'], current_tile.exits)
                #current_tile.exits[dest_tile]
                current_tile = game_map.tiles[dest_tile]
                import pdb; pdb.set_trace()
                continue

            except UnknownDestinationError as ude:
                print(ude)
                continue

except KeyboardInterrupt as e:
    print()
    sys.exit(0)

