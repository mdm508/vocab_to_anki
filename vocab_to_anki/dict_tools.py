from pystardict import Dictionary
from pathlib import Path


def load_dicts(path_to_dict_dir):
    p = Path(path_to_dict_dir)
    dicts = []
    for dict_dir in p.iterdir():
        if dict_dir.is_dir():
            full_path_to_dictionary = next((x.with_suffix("") for x in list(dict_dir.iterdir()) if x.suffix == ".ifo"), None )
            dicts.append(Dictionary(full_path_to_dictionary, in_memory=True))
            print("loaded", full_path_to_dictionary)
    return dicts


def check_dicts(word, dicts):
    """
    looks for word in each dict. the first definition it finds it will use
    if nothing is found returns none
    """
    for d in dicts:
        if word in d:
            return d[word]
    return None 
