"""Wordy

https://exercism.org/tracks/python/exercises/wordy
"""

import operator as op

# to add support for more operations, simply map the function to the op_map
# and add the corresponding desired syntax to the .replace() list in clean_question()
op_map = {
    "++": op.add,
    "--": op.sub, # "-" conflicts with negative ints
    "**": op.mul,
    "//": op.floordiv,
    "^^": op.pow,
}

def answer(question: str) -> int:
    """Calculate answers to word problems LEFT TO RIGHT.
    
    'What is {operand_1} {operation} {operand_2} {operation} ...?'

    !calculations do NOT follow order of operations!
    Supports an arbitrary number of operation actions, including none.
    Supported operations are +: "plus"
                             -: "minus"
                             *: "multiplied by"
                             /: "divided by"
                             ^: "to the power of"

    :param question: - A math word problem.
    :return solution: - The numerical solution to the given `question`.
    """
    q = clean_question(question)                      # format question for parsing
    operands = get_operands(q)                        # extract operands
    operations, _ = get_operations(q)                 # extract operations
    check_question(question, operands, operations)    # check for errors

    solution = operands[0] # ex 'what is 5?' will return 5
    for operator, digit in zip(operations[:], operands[1:]):
        solution = op_map[operator](solution, digit) # call appropriate operation function
        
    return solution

def check_question(question: str, operands: list[int], operations: list[str]) -> None:
    """Check the given `question` for errors.

    :param quesion: - The given word problem to solve.
    :param operands: - Values to perform `operations` on.
    :param operations: - Operations to perform on the `operands`.
    :raise: ValueError - If `question` is malformed or invalid (syntax error), or 
                         contains an unknown operation.
    :return: None
    """
    q = clean_question(question)
    _, unsupported = get_operations(q)
    
    # if the question contains an unknown operation.
    if unsupported:
        raise ValueError("unknown operation")
    
    # if the question is malformed or invalid.
    if (not question.startswith("What is")
        or not question.endswith("?")
        or not operands 
        or len(operations) >= len(operands)
        or len(operands) > len(operations)+1
        or q.endswith(tuple(op_map))
        or q.startswith(tuple(op_map))
       ):
        raise ValueError("syntax error")

def clean_question(question: str) -> str:
    """Format question before parsing.
    
    :param question: - The given word problem to solve.
    :return: - A formatted, parseable string from the given `question`.
    """
    return (question.replace("What is", "")
                    .replace("plus", "++")
                    .replace("minus", "--")
                    .replace("multiplied by", "**")
                    .replace("divided by", "//")
                    .replace("to the power of", "^^")
                    .replace("?", "")
                    .strip())

def get_operands(q: str) -> list[int]:
    """Extract the digits from the question as operands.
    
    :param q: - The formatted given word problem to solve.
    :return: - List of all operands in the given question, `q`.
    """
    return [int(digit) for digit in q.split() if digit.lstrip("-").isdigit()]

def get_operations(q: str) -> list[str]:
    """Extract `supported` and `unsupported` operations from the question.
    
    :param q: - The formatted given word problem to solve.
    :return: - List of all operations in the given question, `q`, and any 
               unsupported (catch-all) operations as well.
    """
    supported = [oper for oper in q.split() if oper in op_map]
    unsupported = [uns for uns in q.split() if uns.isalpha() and uns not in op_map]
    return supported, unsupported
