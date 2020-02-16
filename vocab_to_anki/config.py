import sys 
from pathlib import Path
D_PATH = "/Users/matthewmclaughlin/Documents/Dicts"
CONFIG_PATH = Path.home() / ".vta_rc"

# see README.md for explanation of the format
'''
this file should be cleaned up an implemented more fully 
later on.

it is a way to fool proof loading config so everyone can use it


# rethink how config works
def handle_configure(com):
    match = CONFIGURE_PATTERN.fullmatch(com)
    if match.group(0) == "a" :
        #do stuff related to adding a dictionary
        res = run_config(match.group(1)) #path to dict
        if res == 'q':
            return res
    elif match.group(0) == " ":
        #do stuff related to cinfugring
        pass
    else:
        if match.get_text() == 'q':
            print("please try to congifure again later, exiting")
'''

def verify_vta_rc(lines_in_rc):
    """
    input is a list of lines check the following:
    a) every path exists
    b) the dict dir has at least one .ifo file
    if both are true output true else false
    """
    print(lines_in_rc)
    for p_str in lines_in_rc[1:]:
        p_str = p_str.strip("")
        print(p_str)
        if Path(p_str).exists(): continue
        return False
    dict_path = Path(lines_in_rc[1])
    for d_dir in dict_path.iterdir():
        for file in d_dir:
            print(file)
            if file.suffix == ".ifo":
                return True
    print("h")
    return False

        



def read_vta_rc(path_to_config):
    """
    reads all the lines and returns an array of each line
    """
    def handle_line(line):
        "ignores empty lines, extracts only the path"
        if len(line) <= 1 : return [] 
        return [line.strip().split('=')[1]]

    paths = []
    with open(path_to_config) as file:
        for line in file.readlines():
            paths += handle_line(line)
        return paths
    return paths


def handle_first_time_setup():
    """
    asks for your dictionary path and the output path.
    output path can be left blank and then the funciton will use
    the path to the directory  where config.py is being run.
    """
    print("Reccomended to copy and paste the absolute path")
    dict_dir_path = input("Enter the path to directory of where your dictionaries are stored: ") 
    dict_dir_path = Path(dict_dir_path)
    if dict_dir_path.exists(): return None
    out_path = input("Enter where you would like the .akpg file to be output (press enter for default): ")
    if out_path == "":
        return dict_dir_path, Path(__file__).parent.absolute()
    out_path = Path(out_path)
    if not out_path.exists(): return None
    return dict_dir_path, out_path


def run_config():
    path_to_config = Path.home() / ".vta_rc"
    print(verify_vta_rc(read_vta_rc(CONFIG_PATH)))
    return
    if False and path_to_config.exists():
        with open(path_to_config, 'r') as file_obj:
            for line_num, line in enumerate(file_obj,start=1):
                print(line_num, '\t', line )
    result_paths = handle_first_time_setup()
    if result_paths == None: return None 
    print(result_paths)

#print(run_config())

#
