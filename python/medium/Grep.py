"""Grep

https://exercism.org/tracks/python/exercises/grep
"""

def grep(pattern: str, flags: str="", files: list[str]=[]) -> str:
    """Search files for lines matching a search string and return all matching lines.

    :param pattern: - A string to find within the given `files`.
    :param flags: - Supported flags:
        -n : Prepend the line number and a colon (':') to each line in the output, 
             placing the number after the filename (if present).
        -l : Output only the names of the files that contain at least one matching 
             line.
        -i : Match using a case-insensitive comparison.
        -v : Collect all lines that fail to match.
        -x : Search only for lines where the search string matches the entire line.
    :param files: - The files from which to search for the given `pattern`.
    :return: - Results of the search.
    """
    _n, _l, _i, _v, _x = "-n" in flags, "-l" in flags, "-i" in flags, "-v" in flags, "-x" in flags
    file_count = len(files)
    pattern = pattern.lower() if _i else pattern # case insensitive search flag
    
    lines = list()
    for file in files:
        with open(file) as f:
            for i, line in enumerate(f):
                current_line = line.lower() if _i else line # case insensitive search flag
                out = ""

                # invert search; only output lines with NO pattern matches
                if pattern not in current_line and _v:
                    # it's not necesarry to check the -x flag in an inverse search
                    
                    out = f"{file + ':' if file_count > 1 else ''}{line}"

                    # 41-49 are not necesarry to pass the tests, but you would /expect/ them
                    #   to work with an inverted search, too
                    # insert the line number a pattern match is NOT found on
                    if _n:
                        out = f"{file + ':' if file_count > 1 else ''}{i+1}:{line}"

                    # only output names of files with 1 or more NON pattern matching lines
                    if _l:
                        if f"{file}\n" not in lines:
                            out = file + "\n"
                            lines.append(out)
                        continue
                    
                if pattern in current_line and not _v:
                    # only output whole line pattern matches
                    if _x and pattern != current_line.strip():
                        continue
                        
                    out = f"{file + ':' if file_count > 1 else ''}{line}"

                    # insert the line number a pattern match is found on
                    if _n:
                        out = f"{file + ':' if file_count > 1 else ''}{i+1}:{line}"

                    # only output names of files with 1 or more pattern matching lines
                    if _l:
                        if f"{file}\n" not in lines:
                            out = file + "\n"
                            lines.append(out)
                        continue

                if out:
                    lines.append(out)

    return "".join(lines)
