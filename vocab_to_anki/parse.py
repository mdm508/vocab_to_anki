from bs4 import BeautifulSoup as Bs
import re 
from string import ascii_letters 


DEL_PAT = re.compile("font|img|i|b") # throw these tags away
CONTENT_PAT = re.compile("[a-zA-Z0-9*?+\-!@#$%&()\s;.'\":,=]*") # acceptable content
text = """
hello (also hullo especially in <i>BrE</i>) (<i>BrE</i> also hallo)<br>/   həˈləʊ; <i>NAmE </i>   həˈloʊ/<br> <font color="blue"><i>exclamation</i></font>, <font color="blue"><i>noun</i></font> (pl. -os)<br><img src="9DB12AFC.bmp"> used as a greeting when you meet sb, when you answer the telephone or when you want to attract sb's attention:<br><img src="8CB0DC57.png"><font color="#004080"><i>Hello John, how are you?</i></font><br><img src="8CB0DC57.png"><font color="#004080"><i>Hello, is there anybody there?  </i></font><br><img src="8CB0DC57.png"><font color="#004080"><i><b>Say hello</b> to Liz for me.  </i></font><br><img src="8CB0DC57.png"><font color="#004080"><i>They exchanged hellos (= said hello to each other) and forced smiles. </i></font><br><img src="7E3D5398.bmp"> (<i>BrE</i>) used to show that you are surprised by sth:<br><img src="8CB0DC57.png"><font color="#004080"><i>Hello, hello, what's going on here? </i></font><br><img src="549ED5A0.bmp"> (<font color="green">informal</font>) used to show that you think sb has said sth stupid or is not paying attention:<br><img src="8CB0DC57.png"><font color="#004080"><i>Hello? You didn't really mean that, did you?  </i></font><br><img src="8CB0DC57.png"><font color="#004080"><i>I'm like, ‘Hello! Did you even listen?' </i></font><br>---see also <a href="bword://golden hello">golden hello</a><br>▼ MORE ABOUT<br>greetings<br>Hello is the most usual word and is used in all situations, including answering the telephone.<br>Hi is more informal and is now very common.<br>How are you? or How are you doing? (very informal) often follow Hello and Hi:<br><img src="8CB0DC57.png"><font color="#004080"><i>‘Hello, Mark.' ‘Oh, hi, Kathy! How are you?'</i></font><br>Good morning is often used by members of a family or people who work together when they see each other for the first time in the day. It can also be used in formal situations and on the telephone. In informal speech, people may just say Morning.<br>Good afternoon and Good evening are much less common. Good night is not used to greet somebody, but only to say goodbye late in the evening or when you are going to bed.<br>If you are meeting someone for the first time, you can say Pleased to meet you or Nice to meet you (less formal). Some people use How do you do? in formal situations. The correct reply to this is How do you do?<br><font color="#F14B35"><b>WORD ORIGIN</b></font><br>hello<br> late 19th cent.: variant of earlier hollo.; related to holla.<br>
"""

def extract_base_names(definition_text):
    """
    extracts all of the <img> tags from definition_texst
    and returns a list just the base file names
    """
    return [tag.get("src") for tag in Bs(definition_text, "html.parser").find_all('img')]

def format_for_shell(definition_text):
    """
    trys to make the definitions printed to the shell easier to read
    by removing all the tags
    """
    soup = Bs(definition_text, "html.parser")
    def tags_to_delete(tag):
        if tag.contents: return True
        print(tag)
        return not re.fullmatch(CONTENT_PAT, tag.get_content()) #or not re.fullmatch(DEL_PAT, tag.name)
    for t in soup.find_all(tags_to_delete):
        t.extract()
    return str(soup) 


#print(extract_base_names(text))
print(format_for_shell(text))
#format_for_shell(text)
