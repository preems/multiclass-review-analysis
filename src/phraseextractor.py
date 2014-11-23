phrasePatterns = [
("JJ","NN"),
("JJ","NNS"),
("JJ","NNP"),
("RB","VBN"),
("JJ","JJ","!NN")
]


phrases_list=[]

def searchPhrase(doc,phrase):
	global phrases_list
	for sent in doc:		
		#if len(phrase)==2:
		#	for i in range(1,len(sent)):
		#		if sent[i-1][1]==phrase[0] and sent[i][1]==phrase[1]:
		#			phrases_list.append(sent[i-1:i+1])
		flag=True
		for i in range(len(sent)-len(phrase)+1):
			for j in range(len(phrase)):
				if "!" in phrase[j]:
					flag = True if phrase[j][1:] in sent[i+j][1] else False
				else:
					flag = True if phrase[j]==sent[i+j][1] else False
					if flag==False: break
			if flag==True:
				phrases_list.append(sent[i:i+j+1])




def searchAllPhrases(doc):
	global phrases_list
	phrases_list=[]
	for pattern in phrasePatterns:
		searchPhrase(doc,pattern)
	return phrases_list
	
