import preprocessdoc
import sys
import json

print preprocessdoc.tokenize("Good truck")

with open(sys.argv[1]) as reviews:
	count =0
	for line in reviews:
			jobj = json.loads(line)
			print jobj["text"]
			print preprocessdoc.getAllphrasesDoc(jobj["text"])
			print "\n\n"
			count+=1
			if count==10: break