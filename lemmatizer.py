#preprocess
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import pandas
from nltk.corpus import stopwords
import re
import unicodedata
url = "C:\Users\Akshat\Documents\dumps\company_lemmatize.csv"
#url = "C:\Users\Akshat\Documents\dumps\lemm_all.csv"
data = pandas.read_csv(url,header=None)
dat = data.values
#print dat
x = dat.tolist()
#print type(x)
#print x
X_flat=[]
token =[]
xl=[]
yl=[]


for i in x:
    for j in i:
        X_flat.append(j)    #flattening 

for i in X_flat:
    token.append(word_tokenize(i))

for j in token:                             ####alpha numeric only
    for w in j:
        re.sub('[^A-Za-z0-9]+', '', w)

#print token
bag = ['india','limited','Limited','PRIVATE','LIMITED','ltd','Ltd',
       'ltd.','LTD','LTD.','Ltd.','Pvt.Ltd','PVT.LTD','pvt.ltd',
       'pvt','Pvt','PVT','private','Private','INDIA','co.','CO','CO.','Co.','CO.Pvt','(']
StopBag=["surat",'dubai']
stop = set(stopwords.words('english') + bag + StopBag )
index = None

for i in range(len(token)):
        
        li = token[i]
        for word in li:
            if word in bag :
                index = li.index(word)    ####truncate trailing clutter
                break
            else:
                index = None

        token[i] = li[0:index]

#print token

for lis in token:
    for word in lis:                        #### remove stop words
        if word in stop:
            lis.remove(word)
        else:
            pass
        
#print token


def lemma(x):
    lem = WordNetLemmatizer()
    for i in range(len(x)):                     ##### LEMMATIZE
        for j in range(len(x[i])):
            try:
                x[i][j] = lem.lemmatize(x[i][j]).encode('ascii','ignore')
            except Exception as e:
               print e 
               print j
               #break
            


    return x
tok = lemma(token)
#print tok

lis=[]

def detokenize(y):
    for u in y:
        uc = "".join([" " +r if not r.startswith("'") and r not in string.punctuation else r for r in u]).strip()
        lis.append(uc)
    return lis  

to = detokenize(tok)


def FirstCaps(x):
    for i in range(len(x)):
        x[i] = string.capwords(x[i])
    return x

toke = FirstCaps(to)
print toke

        
        




    

