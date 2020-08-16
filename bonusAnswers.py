from Bio import SeqIO

filename = "sequence.fasta"

write_filename = "longsequences.fasta"

original = SeqIO.parse(filename, "fasta")

new = []
for record in original:
    if len(record.seq) > 200:
        new.append(record)
        
SeqIO.write(new, write_filename, "fasta")