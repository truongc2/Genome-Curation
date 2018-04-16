#Part 3: Find how many times a change in residue of that type and location occurred.
position_dict = {} 
with open("positions.rat") as f: # Input: tab delimited file. 1 Record type: line containing subject_id, subject_residue, query_residue, and position
	for line in f:
		line = line.strip('\n')
		parts = line.split('\t')# list with 4 items
#				[subject_id, subject_sequence_counter, subject_residue, query_residue]
		subject_id = parts[0]
		subject_residue = parts[2]
		query_residue = parts[3]
		location = parts[1]
 
		if subject_id not in position_dict:
			position_dict[subject_id] = {}
			location_dict = position_dict[subject_id]
			location_dict[location] = (subject_residue,{query_residue:1})
			query_dict = location_dict[location][1]
		else:
			location_dict = position_dict[subject_id]
			if location not in location_dict:
				location_dict[location] = (subject_residue,{query_residue:1})
				query_dict = location_dict[location][1]
			else:
				query_dict = location_dict[location][1]	
				if subject_residue not in location_dict[location][0]:
					location_dict[location] = (subject_residue,{query_residue:1})
				else:
					if query_residue not in location_dict[location][1]:
						query_dict[query_residue] = 1
					else:
						query_dict[query_residue] += 1
#print(position_dict)				
# Output of position_dict: {subject_id:{location:(subject_residue,{query_residue:count})}}  
subject_id_list = position_dict.keys()
location_list = []


for subject_id in subject_id_list:
	location_dict = position_dict[subject_id]
	position_list = location_dict.keys()
	for position in position_list:
		position_info = location_dict[position]
		query_dict = position_info[1]
		max_count = max(query_dict.values())
		location_list.append((subject_id, position, max_count, position_info))
													#num	str    num
sorted_list = sorted(location_list, key = lambda x: (-x[2], x[0], int(x[1]))) #max_count, subject_id, position->convert that to integer
for location in sorted_list:
	(subject_id, position, count, position_info) = location  
	(subject_residue, query_info) = position_info
	query_list = []
	for query_residue in query_info.keys():
		query_list.append((query_residue, query_info[query_residue]))
	sorted_query_res = sorted(query_list,key = lambda x: (-x[1], x[0]))  #count, query_res  
	for query_residue, query_count in sorted_query_res:
		print(subject_id + '\t' + position + '\t' + subject_residue + '\t' + query_residue + '\t' + str(query_count))
	print()