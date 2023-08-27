"""Wordy
 
https://exercism.org/tracks/python/exercises/wordy
"""

import operator as op
# to add support for more operations, simply map the function to the OP_MAP
# and add the corresponding desired syntax to the .replace() list in clean_question()
OP_MAP = {
    "++": op.add,
    "--": op.sub, # "-" conflicts with negative ints
    "**": op.mul,
    "//": op.floordiv,
    "^^": op.pow,
}

def answer(question):
    """Calculate answers to word problems LEFT TO RIGHT.
    
    'What is {operand_1} {operation} {operand_2} {operation} ...?'
 
    !calculations do NOT follow order of operations!
    Supports an arbitrary number of operation actions, including none.
    Supported operations are +: "plus"
                             -: "minus"
                             *: "multiplied by"
                             /: "divided by"
                             ^: "to the power of"
 
    :param question: str - A math word problem.
    :return solution: int - The numerical solution to the given `question`.
    """
    record = {"question": question,
              "clean_question": None,
              "operands": None,
              "supported_ops": None,
              "unsupported_ops": None,
    }
    
    return _solve(_check(_parse(_clean(record))))
           
def _clean(record):
    """Format question before parsing."""
    clean = (record["question"].replace("What is", "")
                               .replace("plus", "++")
                               .replace("minus", "--")
                               .replace("multiplied by", "**")
                               .replace("divided by", "//")
                               .replace("to the power of", "^^")
                               .replace("?", "")
                               .strip())
    
    record["clean_question"] = clean
    
    return record

def _parse(record):
    """Extract relevant information needed to check and solve the problem."""
    operands = []
    supported = []
    unsupported = []
    for i in record["clean_question"].split():
        if i.lstrip("-").isdigit():
            operands.append(int(i))
        if i in OP_MAP:
            supported.append(i)
        elif i.isalpha():
            unsupported.append(i)

    record["operands"] = operands
    record["supported_ops"] = supported
    record["unsupported_ops"] = unsupported
    
    return record
    
def _check(record):
    """Check the given `question` for errors."""    
    # if the question contains an unknown operation.
    if record["unsupported_ops"]:
        raise ValueError("unknown operation")
    
    # if the question is malformed or invalid.
    if (not record["question"].startswith("What is")
        or not record["question"].endswith("?")
        or not record["operands"] 
        or len(record["supported_ops"]) >= len(record["operands"])
        or len(record["operands"]) > len(record["supported_ops"])+1
        or record["clean_question"].endswith(tuple(OP_MAP))
        or record["clean_question"].startswith(tuple(OP_MAP))
       ):
        raise ValueError("syntax error")

    return record

def _solve(record):
    """Solve the arithmatic of the word problem from left to right."""
    solution = record["operands"][0] # ex 'what is 5?' will return 5
    
    for operator, digit in zip(record["supported_ops"], record["operands"][1:]):
        solution = OP_MAP[operator](solution, digit) # call appropriate operation function
        
    return solution
