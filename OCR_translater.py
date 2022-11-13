"""OCR number translater

https://exercism.org/tracks/python/exercises/ocr-numbers
"""

def convert(input_grid: list[str]) -> str:
    """Transform OCR numbers 0-9 given through a list of strings to a string of numbers."""    
    OCR_PATTERNS = {
        (" _ ", "| |", "|_|", "   "): "0",
        ("   ", "  |", "  |", "   "): "1",
        (" _ ", " _|", "|_ ", "   "): "2",
        (" _ ", " _|", " _|", "   "): "3",
        ("   ", "|_|", "  |", "   "): "4",
        (" _ ", "|_ ", " _|", "   "): "5",
        (" _ ", "|_ ", "|_|", "   "): "6",
        (" _ ", "  |", "  |", "   "): "7",
        (" _ ", "|_|", "|_|", "   "): "8",
        (" _ ", "|_|", " _|", "   "): "9",
        }
    
    check_dimensions(input_grid)
    OCR_digits = split_OCR_digits(input_grid)
    
    res = []
    for digit in OCR_digits:
        if digit in OCR_PATTERNS:
            res.append(OCR_PATTERNS[digit])
        elif digit == ",":
            res.append(",")
        else: # handle garbled OCR digits
            res.append("?")
    
    return "".join(res).rstrip(",")
    
def split_OCR_digits(grid: list[str]) -> list[tuple[str]]:
    """Split a matrix of strings for OCR digits into individual digits."""
    
    def group(s: str, width: int):
        """Replace `wrap` from textwrap module since wrap wasn't working."""
        return [s[i:i+width] for i in range(0, len(s), width)]
      
    def split_OCR_digit_groups(grid) -> list[tuple[str]]:
        """Split any stacked 'rows' of OCR digits and sign them with a comma {','}."""
        rows = []
        for r in grid:
            if len(r) > 4:
                l = len(r) // 3
                # `grid` will be mangled for multi-row OCR's so we have to unmangle it
                rows.append(tuple(r[i:i + l] for i in range(0, len(r), l)))
    
        # re-mangle: transpose the rows back into the proper order
        rows = zip(*rows)
    
        # insert comma key to know where to add commas
        c_rows = []
        for r in rows:
            c_rows.append(r)
            c_rows.append(",")
    
        # divide rows into each digit representation
        stacked = [tup for row in c_rows for tup in row]
        return stacked
      
    # split each OCR digit from the matrix into it's own representation
    split_grid = list(zip(*[group(row, 3) for row in grid]))
    
    # "rows" of OCR digits
    if x:= split_OCR_digit_groups(split_grid): return x
      
    # single "line" of OCR digits
    return split_grid
  
def check_dimensions(grid: list[str]) -> None:
    """Raise a `ValueError` if the given `input_grid` has inappropriate dimensions."""
    
    if len(grid)%4 != 0:
            raise ValueError("Number of input lines is not a multiple of four")
        
    for row in grid:
        if len(row)%3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
            
