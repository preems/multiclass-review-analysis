import json
import sys

reviewlist = sys.argv[1]
businesslist = sys.argv[2]
catagory = sys.argv[3]

businessIDs={}

with open(businesslist) as businesslist:
	for line in businesslist:
		jboj = json.loads(line)
		print jboj["categories"]
		if catagory in jboj["categories"]:
			businessIDs[jboj["business_id"]]=1

print businessIDs

with open(reviewlist) as reviewfile:
	with open(sys.argv[4],"w") as outputfile:
		for line in reviewfile:
			jboj = json.loads(line)
			if jboj["business_id"] in businessIDs:
				outputfile.write(line)


