#Generate dummy data for a big query table
#using schema provided in txt files.
#Also generate a bq command to load the data into the table

import random, string

field_names = []
types = []

#tab1.txt contains field names line by line
#tab1_types contains field types for the corresponding field names


def get_field_names(f_name):
	f = open(f_name)
	for line in f:
		line = line.strip()
		# if len(line)==0:
		# 	break
		field_names.append(line)
	f.close()

def get_types(f_name):
	f = open(f_name)
	for line in f:
		line = line.strip()
		# if len(line)==0:
		# 	break
		if line.startswith("CHAR"):
			type = "string"
		elif line.startswith("PIC"):
			type = "integer"
		types.append(type)
	f.close()

get_field_names("tab1.txt")
get_types("tab1_types.txt")


#start creating dummy data

def random_word(length):
	return ''.join(random.choice(string.lowercase) for i in range(length))

def random_number():
	return random.randint(0,100000)


#gen_command will generate the command to load data into the table
#input1 of dataset dummydata which also contains the schema

def gen_command():
	cmd = "bq load dummydata.input1 tab1_data.txt "
	schema_list = []
	for i in range(len(field_names)):
		schema_list.append(field_names[i] + ":" + types[i])
	schema_string = ",".join(schema_list)
	cmd += schema_string
	return cmd

#output dummy data into a file
def load_data():
	data = []
	for itr in range(100):
		row = []
		for i in range(len(field_names)):
			# print field_names[i],types[i]
			if types[i]=="string":
				val = random_word(12)
			elif types[i]=="integer":
				val = random_number()
			# print val
			row.append(str(val))
		row_str = ",".join(row)
		# print row_str
		data.append(row_str)

	f = open("tab1_data.txt",'w')
	for el in data:
		f.write(el)
		f.write("\n")
	f.close()


# cmd = gen_command()
# print cmd
# load_data()