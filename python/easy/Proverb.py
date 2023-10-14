"""Proverb

https://exercism.org/tracks/python/exercises/proverb
"""

def proverb(*inputs: list[str], qualifier: str="") -> list[str]:
    """Generate a proverb in the style of, "for want of a nail, the kingdom was lost".

    :param inputs: - The items to build the "proverb" from.
    :param qualifier: - Modifies the final verse for extra flavour.
    :return out: str - The generated "proverb".
    """
    out = []
    for i, thing in enumerate(inputs):
        if i != len(inputs)-1:
            next_thing = inputs[i+1]
            out.append(f"For want of a {thing} the {next_thing} was lost.")
        if i == len(inputs)-1:
            first_thing = inputs[0]
            modified = qualifier+" " if qualifier else ""
            out.append(f"And all for the want of a {modified}{first_thing}.")

    return out
