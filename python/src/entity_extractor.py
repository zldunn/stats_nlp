import spacy
from io_lib import read_cli_query

def main():
    #Make this optional with args
    text = read_cli_query()
    doc = get_doc(text)
    get_entity(doc, True)
    get_nouns(doc, True)


def get_entity(doc, do_print=False):
    # Find named entities, phrases and concepts
    if(do_print):
        print("Printing Entities:")
        for entity in doc.ents:
            print(entity.text, entity.label_)
    return doc.ents

def get_nouns(doc, do_print=False):
    if(do_print):
        print("Printing nouns:")
        for chunk in doc.noun_chunks:
            print(chunk.root)
    return doc.noun_chunks



'''
takes a model name as input and returns the nlp
output: spacey.nlp
'''
def load_langauge(model_name="en_core_web_sm"):
    nlp = spacy.load(model_name)
    return nlp

'''
Takes in doc, and creates an nlp, and inputs the text to the nlp
ouput: Document
'''
def get_doc(text, model_name="en_core_web_sm"):
    nlp = load_langauge(model_name)
    doc = nlp(text)
    return doc

'''
get the entities for a doc of a specific TYPE
return: List[entitiy]
'''
def get_entity_with_type(doc, TYPE=""):
    entities = get_entity(doc)

    if(TYPE != ""):
        filtered = []
        for entity in entities:
            if( TYPE == entity.label_):
                filtered.append(entity)
        return filtered

    return entities



if __name__ == '__main__':
    main()
