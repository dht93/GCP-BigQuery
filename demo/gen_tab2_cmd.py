#Generate a bq command to create an empty table using schema provided in a txt file.
#Data type for all fields is string in this example

field_names = []

def get_field_names(f_name):
	f = open(f_name)
	for line in f:
		line = line.strip()
		# if len(line)==0:
		# 	break
		field_names.append(line)
	f.close()

get_field_names("tab2.txt")

def gen_command():
	cmd = "bq mk --schema "
	schema_list = []
	for i in range(len(field_names)):
		schema_list.append(field_names[i] + ":string")
	schema_string = ",".join(schema_list)
	cmd += schema_string + " -t dummydata.output1"
	return cmd

c = gen_command()
print c