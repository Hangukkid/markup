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

try:
    data = json.loads(open("data.txt", "r").read())
except:
    data = {}

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
    global data           
    for i in range (len(sentences)):
        for j in range (len(sentences[i])):
            if not sentences[i][j] in data:        
                print(i, j) 
                data [sentences[i][j]] = find_character_description (sentences, sentences[i][j])



def setup_text (exclude=[]):
    files = ''
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    
    for book in os.listdir(os.path.join(FILE_PATH, 'books')):
        if book not in exclude:
            book = open(os.path.join(FILE_PATH, 'books', book), encoding = "utf-8")
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
    global data
    try:
        f = json.loads(open("already_done.txt", "r").read())
    except:
        f = []

    files = setup_text(f)
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    
    find_descriptions (files)
    
    list_of_books = []
    for book in os.listdir(os.path.join(FILE_PATH, 'books')):
        list_of_books.append(book)
    
    f = open("already_done.txt", "w+")
    f.write(json.dumps(list_of_books))

    output = open("data.txt", "w+")
    output.write(json.dumps(data))


def compare_data (name1, name2):
    global data
    if data.get(name1) != None and data.get(name2) != None:
        print (euclid_norm_similarity(data[name1], data[name2]))
    else:
        print ("Sample size too small.")

save_data()

print (data.get("raphtalia"))

# print (euclid_norm_similarity(find_character_description_from_files("kill"), find_character_description_from_files("murder")))

# print (find_character_description_from_files("help"))