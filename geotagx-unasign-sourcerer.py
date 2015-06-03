import feedparser
import csv

FEED_URL = "https://asign.cern.ch/resources/georss/nepal_crowd.xml"
print "Attempting to download feed...."
feed = feedparser.parse(FEED_URL)
task_list_size = 0

target_tasks_csv = "tasks.csv"

data_keys = {}
data_row_header = [['id', 'source_uri', 'image_url']]
data_rows = []

print "Attempting to old records from read %s " % (target_tasks_csv)

upgradeMode = False
try:
	f = open("tasks.csv", "r")
	csv_reader = csv.reader(f)
	for row in csv_reader:
		# Maintain a hashmap of image_url -> id in tasks.csv
		data_keys[row[2]] = row[0] 
		data_rows.append(row)
		task_list_size += 1
		upgradeMode = True # Mark as upgrade mode, if even 1 record was collected
	print "%s records read from %s" % (task_list_size, target_tasks_csv)
except:
	# Do nothing, as the file probably doesnot exist
	print "Unable to find %s , hence will attempt to create a fresh %s file" % (target_tasks_csv, target_tasks_csv)


"""
	Fast key searching in a dict using exceptions
"""
def fast_IsAKeyOf(d, key):
	try:
		foo = d[key]
		return True
	except KeyError:
		return False

print "Building new records index from UNASIGN parse......"

for item in feed['entries']:
	"""
		Normalise data to confirm with requirements of pybossa
	"""
	if not fast_IsAKeyOf(data_keys, item['photo']):
		_row = {}

		_row['id'] = task_list_size+1
		task_list_size+=1

		_row['image_url'] = item['photo']

		#TODO : Figure out / Ask the authors of UNASIGN what source they want us to cite
		_row['source_uri'] = item['photo'] 

		row = [_row['id'], _row['image_url'], _row['source_uri']]

		data_keys[_row['image_url']] = _row['id']
		data_rows.append(row)
	else:
		print "Duplicate Entry found. Ignoring photo : %s " % (item['photo'])

print "New records collected. Attempting to write to %s " % (target_tasks_csv)


# Add Header
if not upgradeMode:
	data_rows = data_row_header + data_rows

try:
	f = open(target_tasks_csv, "w")
	csv_writer = csv.writer(f)
	csv_writer.writerows(data_rows)
	f.close()
	print "New tasks file ready at %s " % (target_tasks_csv)
except:
	#Unable to write to file
	print "Unable to write to file, make sure, you have write permissions at the location"