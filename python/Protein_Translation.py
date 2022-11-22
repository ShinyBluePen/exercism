"""Proteins Translation

https://exercism.org/tracks/python/exercises/protein-translation
"""

def proteins(strand: str) -> list[str]:
    """Process an RNA sequence into protein compositions.

    https://en.wikipedia.org/wiki/Translation_(biology)
    
    :param strand: - A string reprisentation of a RNA strand.
    :return polypeptide: - Determined by the RNA strand.
    """
    PROTEINS = {
        "Methionine":    ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine":       ["UUA", "UUG"],
        "Serine":        ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine":      ["UAU", "UAC"],
        "Cysteine":      ["UGU", "UGC"],
        "Tryptophan":    ["UGG"],
        "STOP":          ["UAA", "UAG", "UGA"],
    }
    strand_codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    
    polypeptide = []
    for codon in strand_codons:
        for protein, codons in PROTEINS.items():
            if codon in PROTEINS["STOP"]:
                return polypeptide
            if codon in codons:
                polypeptide.append(protein)
    
    return polypeptide
