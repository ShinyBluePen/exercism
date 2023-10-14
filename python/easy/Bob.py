"""Bob

https://exercism.org/tracks/python/exercises/bob
"""

def response(prompt: str) -> str:
    """Return a response from "Bob" based on prompt and prompt conditions.
    
    :param prompt: str - Propmt presented to Bob.
    :return: str - Bob's response to the given `prompt`.
    """
    # strip any whitespace from orignal string
    comment = prompt.strip()
    
    # abstract questions and shouts
    asking = comment.endswith("?")
    shouting = comment.isupper()
    
    if not comment:
        return "Fine. Be that way!"
    if shouting and asking:
        return "Calm down, I know what I'm doing!"
    if shouting:
        return "Whoa, chill out!"
    if asking:
        return "Sure."
        
    return "Whatever."
