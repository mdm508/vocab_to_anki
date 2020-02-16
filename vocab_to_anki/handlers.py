from constants import *
from dict_tools import check_dicts
from parse import format_for_shell

def pattern_did_match(pattern, command):
    return bool(pattern.fullmatch(command)) 

def sorry(word):
    print('sorry "{}" was not found'.format(word))

def write_to_file(word_list):
    with open(OUTPUT_FILE_PATH, "a") as csvfile:
        writer = csv.writer(csvfile, delimiter= ' ')
        for word, definition in word_list:
            writer.writerow(word, definition)

def handle_quit():
    print("quiting no save")	
    exit(0)

def handle_write_quit(words):
    write_to_file(words)
    print(len(words), "written to", OUTPUT_FILE_PATH)
    exit(0)


def handle_definition_only(com, dicts):
    word = DEFINE_ONLY_PATTERN.fullmatch(com).group(1)
    result = check_dicts(word, dicts)
    if result:
        print(format_for_shell(result))
        return
    sorry(word)

def handle_define_and_add(com, dicts):
    word = DEFINE_ADD_PATTERN.fullmatch(com).group(0)
    result = check_dicts(word, dicts)
    if result:
        definition = result
        print("added", '"{}"'.format(word))
        return [(word,definition)]
    sorry(word)
    return []