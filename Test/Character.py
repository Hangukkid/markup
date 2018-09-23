import CharacterSimilarity
    
def find_all_characters (listofnames, filenames):
    character_descriptions = {};
    for character in listofnames:
        character_descriptions[character] = find_character(filenames, character)
        
    return character_descriptions

def find_character (filenames, name):
    if (not name):
        return {}
    else:
        newname = name.lower()
        return CharacterSimilarity.find_character_description_from_files(filenames, newname)
