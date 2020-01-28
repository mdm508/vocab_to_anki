from pystardict import Dictionary
import os
import csv
import re

OUTPUT_FILE_PATH = "/Users/yuhsinho/dict_to_csv/out.csv"
Q_PAT= re.compile("q")
WQ_PAT = re.compile("wq")
D_PAT = re.compile("d\s([\w|\s]*)")
ADD_PAT = re.compile("[\w|\s]*$")



def check_dicts(word, *dicts):
    """
    looks for word in each dict. the first definition it finds it will use
    if nothing is found returns none
    """
    for d in dicts:
        if word in d:
            return d[word]
    return None 

def make_dict(path_to_dict_dir, dict_file_name):
    path = os.path.join(path_to_dict_dir, dict_file_name)
    return Dictionary(path)	

def write_to_file(word_list):
    with open(OUTPUT_FILE_PATH, "a") as csvfile:
        writer = csv.writer(csvfile, delimiter= ' ')
        for word, definition in word_list:
            write.writerow(word, definition)


def sorry(word):
    print('sorry "{}" was not found'.format(word))
		

def main():
    d1 = make_dict("/Users/yuhsinho/Documents/wq_dicts/stardict-Oxford_Advanced_Learner_s_Dictionary_7-2.4.2", 
	           "Oxford_Advanced_Learner_s_Dictionary_7")
    dicts = d1
    words = [] 
    com = None
    while True:
        com = input("Enter a command: ")
        #try to match, each is mutually eclusive
        ##EXITING COMMANDS
        match = Q_PAT.fullmatch(com) 
        if match:
            print("quiting no save")	
            return
        match = WQ_PAT.fullmatch(com)
        if match:
            write_to_file(words)
            print(len(words), "written to", OUTPUT_FILE_PATH)
            return 
        ##DEFINE WORD COMMANDS <command> <words to define>
        match = D_PAT.fullmatch(com)
        if match:
            print(match.groups())
            word = match.group(1)
            result = check_dicts(word, dicts)
            if result:
                definition = result
                print("definition only, will not be added to word list")
                print(word)
                print(definition)
            else:
                sorry(word)
            continue 
        match = ADD_PAT.fullmatch(com)
        if match:
            word = match.group(0)
            result = check_dicts(word, dicts)
            if result:
                definition = result
                print("added", '"{}"'.format(word))
            else:
                sorry(word)
        else:
            print("you must have entered something weird, try entering something less weird")
            print("only type characters in this range range: [a-zA-Z0-9_ ] ")


            
main()
