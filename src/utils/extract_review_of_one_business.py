import json
import sys
"""
Takes 3 Arguements
* Filename containing all reviews
* Output file name
* Business ID
"""
with open(sys.argv[1]) as reviews:
	with open(sys.argv[2],"w") as out:
		for line in reviews:
				jobj = json.loads(line)
				if jobj["business_id"]==sys.argv[3]:
					out.write(line)
