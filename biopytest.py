#!/usr/bin/env python

from Bio import SeqIO
for seq_record in SeqIO.parse("outgroup sequence.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

my_seq = seq_record.seq

print(repr(my_seq.complement()))
print(repr(my_seq.reverse_complement()))

# uncomment to print the entire sequence:
# print(my_seq)
# print(my_seq.complement())
# print(my_seq.reverse_complement())
