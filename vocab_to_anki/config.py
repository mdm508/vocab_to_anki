import os
from pathlib import Path

path_to_config = Path.home() / ".vta_rc"
if os.path.exists(path_to_config):
    with open(path_to_config, 'r') as file_obj:
        

else:
    # first time set up
    print("please use absolute paths ")
    dir_dicts = input("Enter which directory your dictionaries are in: ")
    out_path = input("Enter where you would like the .akpg file to be output: ")
