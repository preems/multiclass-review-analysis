import preprocessdoc
import sys
import json
from math import ceil
from lexicon import get_score as pol

MINIMUM_THRESHOLD_FOR_TOP_ATTRIBUTE=5

AllAttributes={}


def getTopAttributes(phrases):
	global AllAttributes
	for phrase in phrases:
		if "NN" in phrase[0][1]:
			a=phrase[0][0]
			adj=phrase[1][0]
		elif "NN" in phrase[1][1]:
			a=phrase[1][0]
			adj=phrase[0][0]
		if a not in AllAttributes:
			AllAttributes[a]=[]
		AllAttributes[a].append(adj)

def chooseValidAndTopAttributes():
	global AllAttributes
	topattributes=[]
	for k,v in AllAttributes.items():
		topattributes.append((k,len(v)))
	topattributes.sort(key=lambda x:x[1],reverse=True)

	for key in topattributes[10:]:
		del AllAttributes[key[0]]
	for key in topattributes[:10]:
		if key[1]<MINIMUM_THRESHOLD_FOR_TOP_ATTRIBUTE:
			del AllAttributes[key[0]]
	###
	#print topattributes[:10]
	###
	return topattributes

def prettyPrintTopAttributes():
	for at,val in AllAttributes.items():
		print at,val


def getSentimentFromLexicon():
	print AllAttributes
	for at,val in AllAttributes.items():
		tot=0
		for word in val:
			tot+=pol(word)
		AllAttributes[at]=normaize0to5( tot/len(val) )

def normaize0to5(val):
	return (val+1)*2.5

def returnfinalAttributes(businessID):
	AllAttributes={}
	with open(businessID) as reviews:
		for line in reviews:
			jobj = json.loads(line)
			if jobj["business_id"]==sys.argv[2]:
				getTopAttributes(preprocessdoc.getAllphrasesDoc(jobj["text"]))
		chooseValidAndTopAttributes()
		getSentimentFromLexicon()
		#prettyPrintTopAttributes()
		return AllAttributes



if __name__=="__main__":
	AllAttributes={}
	with open(sys.argv[1]) as reviews:
		for line in reviews:
				jobj = json.loads(line)
				if jobj["business_id"]==sys.argv[2]:
					getTopAttributes(preprocessdoc.getAllphrasesDoc(jobj["text"]))
		chooseValidAndTopAttributes()
		getSentimentFromLexicon()
		prettyPrintTopAttributes()


