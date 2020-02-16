import re 
from bs4 import BeautifulSoup as Bs
from string import ascii_letters 


def extract_base_names(definition_text):
    """
    extracts all of the <img> tags from definition_text
    and returns a list just the base file names
    """
    return [tag.get("src") for tag in Bs(definition_text, "html.parser").find_all('img')]


def format_for_shell(definition_text):
    """
    trys to make the definitions printed to the shell easier to read
    by removing all the tags
    """
    CONTENT_PAT = re.compile(r"""^[\w\s!@#$%^&*()_+,.;:"'\/]*$""") # acceptable content
    DEL_PAT = re.compile("^font|i|ex|c|kref|abr|rref|sub|img|b$") # throw these tags away
    def remove_noisy_tags(soup):
        """
        any tag with text or a purpose not suited for 
        simple definition of word is removed 
        """
        def match_tags_to_delete(t):
            if not re.match(CONTENT_PAT, t.get_text()):
                return True
            if re.match(DEL_PAT, t.name):
                return True 
            return False 
        for t in soup.find_all(match_tags_to_delete):
            t.extract()
    def remove_all_blockquotes(soup):
        """
        remove all the blockquotes from the soup
        """
        def remove_block_tag(block_tag):
            """
            no children and no text means eliminated
            """
            if not block_tag: return
            if not block_tag.content:
                if block_tag.get_text() == "":
                    block_tag.extract()    
                    return
                block_tag.unwrap()
                return
            for b in block_tag.content:
                remove_block_tag(b)
        blocks = soup.find_all('blockquote')
        for b in blocks:
            remove_block_tag(b)
    soup = Bs(definition_text, "html.parser")
    remove_noisy_tags(soup)
    remove_all_blockquotes(soup)
    soup.k.unwrap() #each definition has k tag (for the word)
    return '\n' + soup.prettify() 