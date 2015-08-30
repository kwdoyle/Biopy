#!/usr/bin/env python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# read the fasta file
for seq_record in SeqIO.parse("mouse_mRNA.fasta", "fasta"):
    print(seq_record.id)
    print("Coding Strand:")
    print(repr(seq_record.seq))
    print(len(seq_record))

my_seq = seq_record.seq

# the complement strand
print("Complement:")
print(repr(my_seq.complement()))

# the reverse complement
print("Reverse Complement:")
print(repr(my_seq.reverse_complement()))

# uncomment these to print the entire sequences:
# print(my_seq)
# print(my_seq.complement())
# print(my_seq.reverse_complement())

# this is most likely a round-about way to designate different alphabet
string = str(my_seq)
coding_dna = Seq(string, IUPAC.unambiguous_dna)

# make messenger RNA
m_rna = coding_dna.transcribe()
print("mRNA:")
print(repr(m_rna))

# translated protein sequence
print("Protein Sequence:")
print(repr(m_rna.translate()))

