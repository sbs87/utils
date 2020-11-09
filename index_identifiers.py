import requests
from xml.etree import cElementTree as ET
import time
import csv
import sys
import query_db

input_list=sys.argv[2]
pause_time=int(sys.argv[1]) #5
db=sys.argv[3]


with open(input_list) as input_list_ids:
    ids = csv.reader(input_list_ids, delimiter='\t')
    for row in ids:
        id=row[0]
        time.sleep(pause_time)
        print(query_db.query_db(db,id))
        
