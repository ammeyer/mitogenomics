import os
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "gmarkov17@gmail.com"
filename1 = "japanesefishoca2.fasta"
filename2 = 'mexicantetraoca2.fasta'

if not os.path.isfile(filename1) or (filename2):
    net_handle1 = Entrez.efetch(db="nucleotide", id="NM_001104792", rettype="fasta", retmode="text")
    net_handle2 = Entrez.efetch(db="nucleotide", id="NM_001320209", rettype="fasta", retmode="text")
    out_handle1 = open(filename1, "w")
    out_handle1.write(net_handle1.read())
    out_handle1.close()
    out_handle2 = open(filename2, "w")
    out_handle2.write(net_handle2.read())
    out_handle2.close()
    net_handle1.close()
    net_handle2.close()


record1 = SeqIO.read(filename1, "fasta")
record2 = SeqIO.read(filename2, "fasta")
print(record1,record2)

from Bio import pairwise2
seq1 = SeqIO.read(filename1, 'fasta')
seq2 = SeqIO.read(filename2, 'fasta')
alignments = pairwise2.align.globalms(seq1.seq, seq2.seq, 5, -4, -10, -1)

from Bio.pairwise2 import format_alignment
print(format_alignment(*alignments[0]))
