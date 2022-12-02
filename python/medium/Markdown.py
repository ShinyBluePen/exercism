"""Markdown

https://exercism.org/tracks/python/exercises/markdown
"""

import re

def parse(markdown_input: str) -> str:
    """Parse a formatted string to be marked up with HTML.
    
    Markup supported: Headers #1 - #6
                      __bold text__
                      _italic text_
                      * unordered lists

    :param markdown_input: - String with custom markup.
    :return out: - String formatted in HTML.
    """
    out = ""
    
    for line in markdown_input.splitlines():
        for function in parsers():
            line = function(line)
        out += line

    out = is_unordered_list(out)
    
    return out
    
def parsers():
    """Returns a list of single-line parser functions"""
    return [is_header, is_bold, is_italic, is_list_item, is_paragraph]

def is_paragraph(text: str) -> str:
    """Check if paragraph."""
    tags = re.match("<h|<ul|<p|<li", text)
    return f"<p>{text}</p>" if not tags else text
            
def is_header(text: str) -> str:
    """Check for headers. `#1` - `#6`"""
    headers = {
        "######": f"<h6>{text[7:]}</h6>",
        "#####": f"<h5>{text[6:]}</h5>",
        "####": f"<h4>{text[5:]}</h4>",
        "###": f"<h3>{text[4:]}</h3>",
        "##": f"<h2>{text[3:]}</h2>",
        "#": f"<h1>{text[2:]}</h1>",
    }
    h, *_ = text.partition(" ")
    return headers[h] if h in headers else text

def is_italic(text: str) -> str:
    """Check for `_italic_` text."""
    italic = re.match("(.*)_(.*)_(.*)", text)
    return (f"{italic.group(1)}<em>{italic.group(2)}</em>{italic.group(3)}") if italic else text

def is_bold(text: str) -> str:
    """Check for `__bold__` text."""
    bold = re.match("(.*)__(.*)__(.*)", text)
    return (f"{bold.group(1)}<strong>{bold.group(2)}</strong>{bold.group(3)}") if bold else text

def is_list_item(text: str) -> str:
    """Check for list items. `*`"""
    li = re.match('\* (.*)', text)
    return f"<li>{li.group(1)}</li>" if li else text

def is_unordered_list(text: str) -> str: # credit to jbrr for this function
    """Check for any list items not contained in an unordered list and capture them in one."""
    start = re.search('<li>', text)
    end = re.match('(.*</li>)+', text)
    return f"{text[:start.start()]}<ul>{text[start.start():end.end(0)]}</ul>{text[end.end(0):]}" if start else text
        
