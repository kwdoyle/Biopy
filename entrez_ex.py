from Bio import Entrez

# Need to set email before downloading.
Entrez.email = "YOUR.EMAIL@HERE.COM"

# This will search in the SRA database to find everything related to the Ag-0 arabidopsis individual. It is then possible to pull out the IDs for each of the results.
# I'm not sure if you can use 'prefetch' on these IDs though.
handle = Entrez.esearch(db="sra", term="Ag-0")
record = Entrez.read(handle)
idlist = record["IdList"]

print idlist

