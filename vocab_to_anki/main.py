from pystardict import Dictionary
import os
import csv
import re
from dict_tools import load_dicts, check_dicts 
from parse import format_for_shell
from constants import DICTIONARY_PATH
from handlers import pattern_did_match, handle_quit, handle_definition_only, QUIT_PATTERN, DEFINE_ONLY_PATTERN



def main():
    dicts = load_dicts(DICTIONARY_PATH)
    words = [] 
    com = None
    while True:
        com = input("Enter a command: ")
        if pattern_did_match(QUIT_PATTERN, com): handle_quit()
        #if pattern_did_match(WRITE_QUIT_PATTERN, com): handle_write_quit(com)
        elif pattern_did_match(DEFINE_ONLY_PATTERN, com): handle_definition_only(com,dicts)
        #elif pattern_did_match(DEFINE_ADD_PATTERN): words += handle_define_and_add(com)
        #elif pattern_did_match(CONFIGURE_PATTERN): pass
        else:
            print("you must have entered something weird, try entering something less weird")
            print("only type characters in this range range: [a-zA-Z0-9_ ] ")

            
main()
