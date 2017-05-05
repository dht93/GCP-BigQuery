from google.cloud import bigquery
import uuid
import time


DATASET_NAME = "babynames"
TABLE_NAME = "names_2014"
JOB_NAME = 'dummy-job-'+str(uuid.uuid4())
QUERY = "SELECT name,count FROM babynames.names_2014 WHERE gender = 'M' ORDER BY count ASC LIMIT 6"

client = bigquery.Client(project="bigquerydemo-166705")
#Client objects hold both a project and an authenticated connection 
#to the BigQuery service.

dataset = client.dataset(DATASET_NAME)

if dataset.exists():
	table = dataset.table(TABLE_NAME)
	if table.exists():

		#SYNCHRONOUS QUERYING
		print "Synchronous querying"
		query = client.run_sync_query(QUERY)
		query.run()
		rows = query.rows
		for el in rows:
			print el

		#ASYNCHRONOUS QUERYING
		print "Asynchronous querying"
		job = client.run_async_query(JOB_NAME,QUERY)
		job.begin()
		retry_count = 5
		#polling
		while retry_count > 0 and job.state != 'DONE':
			retry_count -= 1
			time.sleep(10)
			job.reload()
			print job.state
		if job.state=="DONE":
			results = job.results()
			rows = results.fetch_data()[0]
			#fetch_data returns a tuple of a list of rows, total rows and page token
			for el in rows:
				print el

# for dataset in client.list_datasets():
# 	print dataset.name