# Using biopython to do a global pairwise alignment
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

matrix = matlist.blosum62  # is this the cost-matrix?
# gap penalties:
gap_open = -10
gap_extend = -0.5

a = "AAAGCCTTTGCAT"
b = "AAGCGTTTCCAT"

# these are the sequences from the comp. bio lecture notes.
# aligning these using pairwise2 gives the same alignment as the EditDistance function from the edit distance.py script
Y = "AAGGTATGAATC"
X = "AACGTTGAC"



# the 'ds' in align.globalXX means: A (d)ictionary returns the score of any pair of characters and (s)ame open and extend gap penalties for both sequences.
# help regarding pairwise2 was found at http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html
algn = pairwise2.align.globalds(a, b, matrix, gap_open, gap_extend)
# pairwise2 will show all possible optimal alignments
best_align = algn[0]
print("Best alignment:")
print(best_align)
print algn
# make nicer formatted alignment
for i in algn:
    print(pairwise2.format_alignment(*i))  # the * takes all the values in the list and passes them as arguments for the function.
