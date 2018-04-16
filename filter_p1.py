#Part 1: Find best matches
import re

query = ""
subject = ""
best_match = 0


with open("In_WT.eq.6-9.trim.blastn.rat") as f: # Input file with three record types: Query line, Subject line, and HSP line
	for line in f: 
		line = line.strip("\n")
		
		if re.search(r'^Query', line): # Query line: Query=   query_id	query_def	query_len
			query = ""
			subject = ""
			best_match = 0
			query = line
		
		elif re.search(r'^>', line):  # Subject line: >	  subject_id  subject_def	subject_len
			if query != "":
				subject = line
			else:
				continue 
	
		elif re.search((r'^HSP'), line): # HSP line:
#	Index  	   0        1         2       3        4         5            6           7        8 ...
#	HSP line: HSP	bit_score	evalue	n_seq	evalue2   align_len   identities   positives  gaps ...
#				
#...      	   9        10           11          12           13            14           15
#...      	 strand   query_beg    query_end    query    subject_beg    subject_end    subject
		
			if subject != "" and best_match == 0: 
				hsp_parts = line.split("\t") # list of hsp parts
				if hsp_parts[5] != hsp_parts[6]: # align_len not equal to identity
					best_match = int(hsp_parts[1])
					print(subject + "\t" + line.upper()) # Outputs a tab delimited line containing Subject and HSP 
				else:
					query = ""
					subject = ""
			elif subject != "" and best_match > 0:
				hsp_parts = line.split("\t")
				if int(hsp_parts[1]) == best_match:  # Match equally good
					best_match = int(hsp_parts[1])
					print(subject + "\t" + line.upper()) 
				else:
					continue
			elif query == "" or subject == "":
				continue