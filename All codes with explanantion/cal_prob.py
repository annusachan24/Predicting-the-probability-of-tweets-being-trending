# encoding=utf8
import gensim,time
from gensim import models
from gensim.models import Doc2Vec
from gensim.models.doc2vec import DocvecsArray
import numpy as np

start_time = time.time()
#load the model
model= Doc2Vec.load('my_model_5train.doc2vec')
print "model loaded"
a=1
b=7000
c=7001
d=11590

def avg(k):
    #print "k is ",k
    #print "i m getting called"
    sum_cosine=0
    b=7000
    for j in range (0,7000):
        #print "j is ",j
        s_cosine=model.docvecs.similarity(j,k)
        sum_cosine=sum_cosine+s_cosine
    avg_cosine=sum_cosine/b
    return avg_cosine

aa=np.zeros(d-c+1)
bb=np.zeros(d-c+1)
#qwerty=avg(7001)
#print "adbgfdgh ; ",qwerty
# calculating avg cosine similarities
for i in range(7001,11590):
   # print i
    aa[i-7001]=avg(i)
    if (aa[i-7001]>0.01):
        bb[i-7001]=1
    else:
        bb[i-7001]=2
print"avg similarity calculated"

for i in range(0,4590):
    print bb[i]

#cls to classes
y=0
classes =np.zeros(11590)
f=open('cls1.txt','r')

for lines in f:
    line=lines.split()
    #print line[0]
    classes[y]=float(line[0])
    y=y+1
print "size of classes is ", classes.shape

#for l in classes:
   #print l

'''
classes=np.loadtxt(f)
for l in classes:
    print l
print "size is ", classes.shape
'''
comp_cls= np.zeros(4590)
for i in range(0,4590):
    comp_cls[i]=classes[i+7000]
    

#for m in comp_cls:
    #print m

print "size of comp_cls is ", comp_cls.shape


count=0;
for i in range(4590):
    if(bb[i]==comp_cls[i]):
        count=count+1
print "count is : ",count
acc=count*100/4590
print "accuracy is : ", acc

print("--- %s seconds ---" % (time.time() - start_time))
