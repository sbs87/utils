import requests
from xml.etree import cElementTree as ET
import time
import csv

def query_db(db,id):
    output=""
    webenv_url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db='+db+'&term='+id+'&usehistory=y'
    
    try:
        resp = requests.get(webenv_url)
        root=ET.XML(resp.text)
        we=root.find('WebEnv')
        query_wenv=we.text
        query_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db="+db+"&webenv="+query_wenv+"&query_key=1&rettype=abstract&retmode=text"
        ## Buried in this URL is the gene's symbol. FInd it. 
        qeury_resp = requests.get(query_url)
        #soup = BeautifulSoup(qeury_resp.content, 'html.parser')
        # gene name start and stop
        tmp=qeury_resp.text#.replace("\n","")
        start=tmp.find('\n.1 "') + 5 # 861
        end=tmp.find(";",start)# - 1
        output=tmp[start:end]
    except:
        output="ERROR"
    out_line="PUBCHEM.COMPOUND:"+id+"\t"+output
    return(out_line)


        
