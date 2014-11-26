phrasePatterns = [
("JJ","NN"),
("JJ","NNS"),
("JJ","NNP"),
("RB","VBN"),
("JJ","JJ"),
("RB", "NN"),
("RB", "NNS"),
("RB", "NNP"),
("RB", "JJ"),
("NN", "VBP"),
("NNS", "VBP"),
("NNP", "VBP"),
("NN", "JJ"),
("NNS", "JJ"),
("NNP", "JJ"),
("VB", "JJ"),
("RB", "VB")
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
		#for i in range(len(sent)-len(phrase)+1):
		i = 0
		while i < len(sent)-len(phrase)+1:
			for j in range(len(phrase)):
				if "!" in phrase[j]:
					flag = True if phrase[j][1:] in sent[i+j][1] else False
				else:
					flag = True if phrase[j] in sent[i+j][1] else False
					if flag==False: break
			if flag==True:
				phrases_list.append(sent[i:i+j+1])
				i += len(phrase)
			
			i += 1

def searchAllPhrases_new(doc):
	global phrases_list
	phrases_list=[]
	for sent in doc:
		i = 0
		while i < len(sent)-1:
			phraseExtracted = (sent[i][1], sent[i+1][1])
			if phraseExtracted in phrasePatterns:
				phrases_list.append(sent[i:i+2])
				#phrases_list.append(sent[i+1])
				i += 2
			else:
				i += 1

	return phrases_list

def searchAllPhrases(doc):
	global phrases_list
	phrases_list=[]
	for pattern in phrasePatterns:
		searchPhrase(doc,pattern)
	return phrases_list
	
