import json
with open('doid.json') as f:
	x=json.load(f)
#print(x)
#print(x['graphs'][0]['nodes'])
for i in x['graphs'][0]['nodes']:
	try:
		print(i['id']+"\t"+i['lbl'])
	except:
		print(i['id']+'\tnot_found')
	#print(i)
