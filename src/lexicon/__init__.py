
def get_weight(polarity, weight):
    return 0 if 'neutral' in polarity else 0.5 if 'positive' in polarity and 'weak' in weight else 1.0 if 'positive' in polarity and 'strong' in weight else -0.5 if 'weak' in weight else -1.0

def get_terms(line):
    return line.split()

def get_score(word):
    global hashed
    return hashed[word] if word in hashed else 0

def hashContents(filepath):

    global hashed
    f = open(path)

    for line in f:
        terms = get_terms(line)
        word = terms[2][terms[2].find('=')+1:]
        sentimentType = terms[5][terms[5].find('=')+1:]
        sentimentWeight = terms[0][terms[0].find('=')+1:]

        hashed[word] = get_weight(sentimentType, sentimentWeight)

    return         

hashed={}    
path = "lexicon/mpqa.tff"
hashContents(path)

if __name__ == "__main__":

    #path = "mpqa.tff"
    #hashed = hashContents(path)

    word = "terrible"
    print get_score(word)
