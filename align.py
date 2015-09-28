#!/usr/bin/env python

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

matrix = matlist.blosum62

# gap penalties:
gap_open = -10
gap_extend = -0.5

def align(X, Y):
    algn = pairwise2.align.globalds(X, Y, matrix, gap_open, gap_extend)
    best_align = algn[0]
    return best_align
