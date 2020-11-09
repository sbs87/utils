import requests
from xml.etree import cElementTree as ET
import time
import csv
import sys
pause_time=int(sys.argv[1]) #5
output=""
input_list=sys.argv[2]
with open(input_list) as ncbigenes:
    ids = csv.reader(ncbigenes, delimiter='\t')
    for row in ids:
        id=row[0]

## First, get the webrnv xml
#id="2"

#for i in range(1,100,1):
        time.sleep(pause_time)
        #id=str(i)
        db=sys.argv[3] #"gene"
        webenv_url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db='+db+'&term='+id+'&usehistory=y'
        try:
            resp = requests.get(webenv_url)
            root=ET.XML(resp.text)
            we=root.find('WebEnv')
            query_wenv=we.text

            query_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db="+db+"&webenv="+query_wenv+"&query_key=1"

            ## Buried in this URL is the gene's symbol. FInd it. 
            qeury_resp = requests.get(query_url)
            #soup = BeautifulSoup(qeury_resp.content, 'html.parser')
            # gene name start and stop
            tmp=qeury_resp.text.replace("\n","")
            start=tmp.find('locus "') + 7 # 861
            end=tmp.find(",",start) - 1
            output=tmp[start:end]
        except:
            output="ERROR"

        print("NCBIGENE:"+id+"\t"+output)
