"""RNA Transcription

https://exercism.org/tracks/python/exercises/rna-transcription
"""

def to_rna(dna_strand: str) -> str:
    """Transcribe a DNA strand to an RNA strand.
    
    :param dna_strand: str - The given DNA strand to convert.
    :return: str - The RNA strand transcribed from the given `dna_strand`.
    """
    N_MAP = {k: v for k, v in zip("GCTA", "CGAU")}
    return "".join([N_MAP[n] for n in dna_strand])
