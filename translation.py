from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import Bio.SeqUtils
from Bio.Data import IUPACData
from Bio.Data import CodonTable

my_seq = Seq('AGGCGCTATCCCTATCCAACTGGGGAC', IUPAC.unambiguous_dna)
mRNA = my_seq.transcribe()

print("DNA:")
print(repr(my_seq))
print("RNA:")
print(repr(mRNA))
print("Sequence of amino acids, aka a protein:")
print(repr(mRNA.translate()))

# this is here to show the key for what letters represent which amino acid
print("Amino acid key:")
print(IUPACData.protein_letters_1to3)

# here is now to display the codon translation table:
standard_table = CodonTable.unambiguous_dna_by_id[1]
print(standard_table)
