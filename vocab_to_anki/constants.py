from re import compile
# path related contants
OUTPUT_FILE_PATH = "/Users/yuhsinho/dict_to_csv/out.csv"
DICTIONARY_PATH = "/Users/matthewmclaughlin/Documents/Dicts"

# pattern constants
QUIT_PATTERN= compile("q") 
WRITE_QUIT_PATTERN = compile("wq")
DEFINE_ONLY_PATTERN = compile(r"d\s([\w|\s]*)")
DEFINE_ADD_PATTERN = compile(r"[^cf](\w|\s)*")
#CONFIGURE_PATTERN = re.compile(r"cf\s(a|a=|\s)(.)*")