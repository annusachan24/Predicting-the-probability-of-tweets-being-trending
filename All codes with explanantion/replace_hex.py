# replced ?,. by ''
# converted file into utf-8 format in notepad++
# now replace x85 by '' and i was relacing one by one
# #being stupid
# used the range [^\x00-\x7F]+
import gensim,time
from gensim import models
from gensim.models import Doc2Vec
from gensim.models.doc2vec import DocvecsArray
import numpy as np
import re

start_time = time.time()
f1 = open('lower_case.txt', 'r')
f2 =open('lower_replaced.txt', 'w')
for line in f1:
    #f2.write(line.replace('\x85','').replace('\x93','').replace('\xed','').replace('\xe9','')) // there were so many of them
    f2.write(re.sub(r'[^\x00-\x7F]+','',line))
print "here 2"
f1.close()
f2.close()



print("--- %s seconds ---" % (time.time() - start_time))

