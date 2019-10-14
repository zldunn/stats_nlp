from entity_extractor import get_entity_with_type, get_doc
from io_lib import read_cli_query
from Mapper import Mapper
from StatQuery import StatType, StatQuery
import spacy

def main():
    text = read_cli_query()
    process_query(text)

'''
Takes text as input and processes the process_query
Should return the statistics you want
'''
def process_query(text):
    doc = get_doc(text)
    players = get_player_from_doc(doc)
    # just_names = get_players_names(players)
    # print(just_names)
    player = players[0]
    stat_type = get_stat_type(doc, players)
    query = StatQuery(player.text, stat_type)
    print(query.as_dict())

'''
returns list of entities for a doc
Return: List[Token]
'''
def get_player_from_doc(doc):
    name_type = "PERSON"
    players = get_entity_with_type(doc,name_type)
    return players

'''
Returns the type of stat type for a given doc
input:
doc - doc
players - List[Tokens]
'''
def get_stat_type(doc, players):
    # Since the player is already accounted for, but also a noun, lets filter
    # them from the nouns
    nouns = list(doc.noun_chunks)
    noun_roots = [noun.root for noun in nouns]
    players_roots = [player.root for player in players]
    filtered = [noun  for noun in nouns if noun not in players]

    mapper = Mapper()
    print(list(nouns))

    for token in list(filtered):
        noun_root = token.root
        print(list(filtered))
        if noun_root.text in mapper.yards:
            return yardage_type(noun_root)
    return StatType.EMPTY

'''
Given a 'yard' token, will parse the parent, left, and right to see the type of
yards
Returns: StatType
'''
def yardage_type(yard_tok):
    # Look left, right, and then parent of word
    mapper = Mapper()
    print(yard_tok)

    for left in list(yard_tok.lefts):
        print(left)
        if left.text in mapper.passing:
            return StatType.PASS_YDS
        elif left.text in mapper.rushing:
            return StatType.RUSH_YDS

    for right in list(yard_tok.rights):
        print(right)
        if right.text in mapper.passing:
            return StatType.PASS_YDS
        elif right.text in mapper.rushing:
            return StatType.RUSH_YDS

    parent = yard_tok.head
    if parent.text in mapper.passing:
        return StatType.PASS_YDS
    elif parent.text in mapper.rushing:
        return StatType.RUSH_YDS
    return StatType.TOT_YDS

def get_tokens_text(token_list):
    return [token.text for token in token_list]

if __name__ == '__main__':
    main()
