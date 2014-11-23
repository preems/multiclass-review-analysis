from nltk import word_tokenize as wtok
from nltk import pos_tag as pos
from nltk import sent_tokenize as stok
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import phraseextractor 
#from stepwords import step_words

stop_words=['is','a','who','has','was','that','to','for','are','and','the']


def tokenize(doc):
	stemmer = SnowballStemmer('english')
	lemmatizer = WordNetLemmatizer()
	processed_doc=[]
	processed_sent=[]
	sents = stok(doc)
	for sent in sents:
		wtoks =wtok(sent)
		for tok in wtoks:
			if tok not in stop_words:
				processed_sent.append(tok.lower())
				#processed_sent.append(stemmer.stem(tok))
		processed_sent=pos(processed_sent)
		processed_doc.append(processed_sent)
		processed_sent=[]
	return processed_doc

def getAllphrasesDoc(doc):
	return phraseextractor.searchAllPhrases(tokenize(doc))
