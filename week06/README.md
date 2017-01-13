### November 28 ###
* Stand up
* Sequence alignment with [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi)
 * [chimp1](https://www.ncbi.nlm.nih.gov/nuccore/JF727179.2) vs [chimp2](https://www.ncbi.nlm.nih.gov/nuccore/JF727176.2)
 * [human](https://www.ncbi.nlm.nih.gov/nuccore/GU170821.1) vs [chimp](https://www.ncbi.nlm.nih.gov/nuccore/JF727179.2)
 * Find your own! How about squamata (snakes and lizards)
* Sequence alignment with [Biopython](http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html)
 * try shorter sequences then try the ones above
 * Local vs. Global alignments: Global alignments, which attempt to align every residue in every sequence, are most useful when the sequences in the query set are similar and of roughly equal size. (This does not mean global alignments cannot start and/or end in gaps.) A general global alignment technique is the Needleman–Wunsch algorithm, which is based on dynamic programming. Local alignments are more useful for dissimilar sequences that are suspected to contain regions of similarity or similar sequence motifs within their larger sequence context. The Smith–Waterman algorithm is a general local alignment method also based on dynamic programming.[link](https://en.wikipedia.org/wiki/Sequence_alignment#Global_and_local_alignments)
* Forward and backward thinking ... what did we do last week that you can continue working on? what can you do now to make next week easier?
 * Hint! How to query genbank within a python script
 * Hint! Thinking about database design for genes and genomes

### November 30 ###
* What did we do Monday?
* Pseudocode --> code : compare nuclear genes to mitochondrial genes for base content
* What makes a downloaded sequence 'better'? Brainstorm
* Continue to work on monday work
