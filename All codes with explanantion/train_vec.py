# encoding=utf8

import gensim,future
import time
from gensim import models
#from gensim.models.doc2vec import TaggedLineSentence now taggedlinesentences is replaced by TaggedLineDocument
from gensim.models.doc2vec import TaggedLineDocument
from gensim.models import Doc2Vec
#from future import unicode_literals

start_time = time.time()



sentences = TaggedLineDocument('lower_replaced.txt')



print "Training......\n"
model = Doc2Vec(alpha=0.025, min_alpha=0.025)# use fixed learning rate
print "here.............@@@@@@@@@@@@@@ \n"

model.build_vocab(sentences)


for epoch in range(5):
    model.train(sentences)
    model.alpha -= 0.002  # decrease the learning rate
    print model.alpha
    model.min_alpha = model.alpha  # fix the learning rate, no decay
print "traning done \n"
model = Doc2Vec(sentences)
model.save('my_model_5train.doc2vec')


print("--- %s seconds ---" % (time.time() - start_time))

# model= Doc2Vec.load('my_model.doc2vec')
# model.docvecs[27] it gives the vector of 27th document
