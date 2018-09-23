
import gzip
import gensim
import os
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def textToGzip(input_file):
    with open (input_file, "r") as myfile:
        data=myfile.read().replace('\n', ' ')
        data = bytes(data)
        with gzip.open(os.getcwd() + input_file, 'wb') as f:
            f.write(data)

def read_input(input_file):
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} lines".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

if __name__ == "__main__":
    model = gensim.models.Word2Vec.load("word2vec.model")
    
    curDir = os.getcwd()
    train_path = curDir + "/train"
    trainOld_path = curDir + "/trainOld"
    for path,dirs,files in os.walk(train_path):
        for filename in files:
            documents = list (read_input ("train/" + filename))
            os.rename(train_path + '/' + filename, trainOld_path + '/' + filename)
            logging.info ("Done reading data file")
            model.train(documents,total_examples=len(documents),epochs=10)
    logging.info ("Done training, saving model")
    model.save("word2vec.model")