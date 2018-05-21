# Genome-Curation of Salmonella typhi
Summary: Comparison of subject and query sequence in Salmonella typhi. Curate the data and look for changes in the DNA sequence. Find how many times the change occurred and the downstream effects on the amino acids and proteins. 

Part 1:
Go through the BLAST file that contains three entry types: Query, Subject, HSP. For each Query, see if there is a matching Subject and a matching HSP. If there is no matching Subject or HSP, delete the Query. If there is a Subject and HSP, check if the assigment length is not equal the identity, save the Query, Subject, and HSP. If the following line is an HSP, check if the bit score is just as good or better than the current HSP score. Print the Subject and the corresponding HSP lines. Save the output to another file (matches). 


Part 2: 
Go through the matches files that contains two record types: Subject and HSP. There are two directions to the DNA strand, negative and positive. Go through both the query sequence and subject sequence and look for any differences. If the strand is in the negative direction, find the complement of the strand to get the forward direction. Print and output the SubjectID, subject residue, query residue, and the position of the change into a newfile (positions)

Part 3: 
