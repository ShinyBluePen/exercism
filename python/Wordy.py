"""Wordy
 
https://exercism.org/tracks/python/exercises/wordy
"""

OP_MAP = {
    "multiplied by": "__mul__",
    "divided by": "__truediv__",
    "plus": "__add__",
    "minus": "__sub__",
    "to the power of": "__pow__",
}
PREFIX = "What is"
SUFFIX = "?"

def answer(question: str) -> float:
    """Calculate answers to word problems LEFT TO RIGHT.
    
    'What is {operand_1} {operation} {operand_2} {operation} ...?'
 
    !calculations do NOT follow order of operations!
    Supports an arbitrary number of operation actions, including none.
    Supported operations are "plus"
                             "minus"
                             "multiplied by"
                             "divided by"
                             "to the power of"
 
    :param question: - A math word problem.
    :return: - The numerical solution to the given `question`.
    """
    return solve(*parse(question))
    
def parse(question: str) -> tuple[list[float], list[str]]:
    """Clean and extract relevant information needed to solve the `question`."""
    for english, operator in OP_MAP.items():
        question = question.replace(english, operator)
        
    question = question.removeprefix(PREFIX).removesuffix(SUFFIX).split()
    
    # modular logic: even indicies for operands, odd for supported operations
    operands, supported_ops = [], []
    for i, token in enumerate(question):
        if token.isalpha() and token not in OP_MAP.values():
            raise ValueError("unknown operation")
            
        elif not i % 2: # even indicies
            if not token.removeprefix("-").isnumeric():
                raise ValueError("syntax error")
            operands.append(float(token))
            
        elif i % 2: # odd indicies
            if token not in OP_MAP.values():
                raise ValueError("syntax error")
            supported_ops.append(token)
            
    # there must be more operands than operations
    if len(operands) <= len(supported_ops):
        raise ValueError("syntax error")
    
    return operands, supported_ops
    
def solve(operands: list[float], operations: list[str]) -> float:
    """Solve the arithmetic of the word problem given to `answer()` from left to right."""
    # ex 'what is 5?' will return 5
    solution = operands[0] 
    
    # call appropriate operation function
    for operator, digit in zip(operations, operands[1:]):
        solution = solution.__getattribute__(operator)(digit)
        
    return solution
