# PART 2: Identify the matches and its location 
with open("matches.rat") as f: # Input is tab delimited file with 1 record type: line with Subject and HSP
	for line in f:
		line = line.strip("\n") 
		data_parts = line.split("\t") # List with 20 items
# Index     0       1           2            3        4       5        6       7        8        9
#		  [ >, subject_id, subject_def, subject_len, HSP, bit_score, evalue, n_seq, evalue2, align_len ...
#                   10         11       12     13       14         15       16       17            18         19
#          ... identities, positives, gaps, strand, query_beg, query_end, query, subject_beg, subject_end, subject ]

		subject_id = data_parts[1]
		direction = data_parts[13] 
		subject_begin = int(data_parts[17]) 
		query_sequence = data_parts[16]
		subject_sequence = data_parts[19]
		
		subject_sequence_counter = subject_begin 
		subject_step = 1 if direction == "+" else -1

		dna_complement = {
									"A":"T",
									"T":"A",			
									"G" :"C",
									"C":"G",
									"N":"N",
									"a":"T",
									"t":"A",
									"g":"C",
									"c":"G",
									"-":"-",
											}
		
							
		    																		      # Iterator:        1234   |      1         2         3         4
		for (query_residue,subject_residue) in zip(query_sequence,subject_sequence):      # subject_sequece: GACA   |    (G,G)     (A,A)     (C,C)	   (A,T)   
			if subject_residue != query_residue:                                          # query_sequence:  GACT   |
				if direction == "-":
					subject_position = subject_id + '\t' + str(subject_sequence_counter) +'\t'+ dna_complement[subject_residue] + '\t'+ dna_complement[query_residue] 
					if query_residue != "N" and query_residue != "-":                                     #  subject_id  position sres qres 
						print(subject_position) # Output: tab delimited string --->  NC_016856   2152430  T    C    
						subject_sequence_counter += subject_step
					else:
						continue
				else: #if the direction == "+"
					subject_position = subject_id + '\t' + str(subject_sequence_counter) + '\t'+ subject_residue + '\t'+ query_residue 
					if query_residue != "N" and query_residue != "-":
						print(subject_position)
						subject_sequence_counter += subject_step
					else:
						continue	
			elif subject_residue == query_residue:
				subject_sequence_counter += subject_step