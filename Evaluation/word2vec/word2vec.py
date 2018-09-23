
import gzip
import gensim
import logging

model = gensim.models.Word2Vec.load("word2vec.model")

w1 = ["shocked"]
print(w1)
out = model.wv.most_similar (positive=w1, topn=6)
print(out)

w1 = ["bed",'sheet','pillow']
w2 = ['couch']
print(w1)
print(w2)
out = model.wv.most_similar (positive=w1,negative=w2,topn=10)
print(out)