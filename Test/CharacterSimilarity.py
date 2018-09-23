import math, os, json
# Imports
import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
# stopwords.extend(string.punctuation)  

def norm(vec):
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    key1 = vec1.keys()
    key2 = vec2.keys()
    num = 0
    for i in key1:
        for j in key2:
            if i == j:
                num += vec1[i]*vec2[j]
    den = norm(vec1)*norm(vec2)
    return (num/den)
                
def euclid_similarity(vec1, vec2):
    v_euc = {}
    for i,j in vec1.items():
        v_euc[i] = j
        
    for i in vec2.keys():
        if i in v_euc.keys():
            if (not vec1[i] == 1) and (not vec2[i] == 1):
                v_euc[i] = vec1[i] - vec2[i]
    return norm(v_euc)
    

def euclid_norm_similarity(vec1, vec2):
    
    v1new = {}
    for i,j in vec1.items():
        v1new[i] = j
        
    v2new = {}
    for i,j in vec2.items():
        v2new[i] = j
    
    for i in v1new.keys():
        v1new[i] = v1new[i]/(norm(v1new))
        
    for i in v2new.keys():
        v2new[i] = v2new[i]/(norm(v2new))
    
    return euclid_similarity(v1new, v2new)
    
    
    
def find_character_description(sentences, name):
    description = {}
 
    for i in range (len(sentences)):
        if name in sentences[i]:
            for j in range (len(sentences[i])):
                if name != sentences[i][j]:
                    if sentences[i][j] != '':
                        if sentences[i][j][0].isalpha():
                            if sentences[i][j] in description.keys():
                                description[sentences[i][j]] += 1
                            else:
                                description[sentences[i][j]] = 1                 


    return description
            
def find_descriptions (sentences):
    description = {}              
    for i in range (len(sentences)):
        for j in range (len(sentences[i])):
            if not j in description:
                description [j] = find_character_description (sentences, j)

    return description


def setup_text (exclude=[]):
    files = ''
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    
    for book in os.listdir(os.path.join(FILE_PATH, 'books')):
        if book not in exclude:
            book = open(os.path.join(FILE_PATH, 'books', book), encoding = "latin1")
            files += ' ' + book.read()
    
    files = files.lower()
    files = files.replace('!', '.')
    files = files.replace('?', '.')
    files = files.replace(';', '')
    files = files.replace('…', '')
    files = files.replace(':', '')
    files = files.replace('--', ' ')
    files = files.replace('-', ' ')
    files = files.replace(',', '')
    files = files.replace('\n', ' ')
    files = files.replace(')', '')
    files = files.replace('(', '')
    files = files.replace(']', '')
    files = files.replace('[', '')
    files = files.replace('{', '')
    files = files.replace('}', '')
    files = files.replace('/', '')
    files = files.replace('\\', '')
    files = files.replace('“', '')
    files = files.replace("”", '')
    files = files.replace('"', '')
    # files = files.replace('"', '')
    files = files.replace('0', '')
    files = files.replace('1', '')
    files = files.replace('2', '')
    files = files.replace('3', '')
    files = files.replace('4', '')
    files = files.replace('5', '')
    files = files.replace('6', '')
    files = files.replace('7', '')
    files = files.replace('8', '')
    files = files.replace('9', '')
    
    for s in stopwords:
        files = files.replace(" " + s + " ", ' ')

    files = files.split('.')
    
    for j in range (len(files)):
        files[j] = files[j].split(' ')
    
    return files


def find_character_description_from_files(name):
    return find_character_description(setup_text(), name)


def save_data ():
    files = setup_text()
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))

    list_of_books = []
    for book in os.listdir(os.path.join(FILE_PATH, 'books')):
        list_of_books.append(book)
    
    f = open("demofile.txt", "a")
    f.write("Now the file has one more line!")



# print (euclid_norm_similarity(find_character_description_from_files("kill"), find_character_description_from_files("murder")))

# print (find_character_description_from_files("help"))