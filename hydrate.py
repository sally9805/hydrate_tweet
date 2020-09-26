import csv
import twarc

t = twarc.Twarc() # Use Twarc Python lib

def ids(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			yield row[0]

def id_sentiment_dict(filename):
	id_sentiment_dict = {}
	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			id_sentiment_dict[int(row[0])] = float(row[1])
	return id_sentiment_dict

filename = 'march31_april1.csv' #change the input file here
id_sentiment_dict = id_sentiment_dict(filename)
output_name = filename.split('.')[0]+'_cs229_data.csv'
with open(output_name, 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter = ',')
	writer.writerow(['id','sentiment','country','coordinates'])
	for tweet in t.hydrate(ids(filename)):
		if tweet['place'] is not None and tweet['place']['country_code'] == 'US':
			writer.writerow([tweet["id"], id_sentiment_dict[tweet["id"]], 'US', tweet['geo']['coordinates']])
