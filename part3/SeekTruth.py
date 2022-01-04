# SeekTruth.py : Classify text objects into two categories
#
# Arpita Welling (aawellin), Aditi Gode (adigode), Sanika Paranjpe (sparanjp)
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys
from collections import defaultdict
import re
import math


def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}


#This function is used to tokenize data, remove punctuations, remove numbers, and remove certain stop words
def data_preprocessing(sentence):
    stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "youre", "youve", "youll", "youd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "shes", 'her', 'hers', 'herself', 'it', "its", 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "thatll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "dont", 'should', "shouldve", 'now', 'd', 'll','ill', 'm', 'o', 're', 've', 'y', 'ain',  'needn','also', "neednt", 'shan', "shant", 'shouldn', 'wasn', "wasnt", 'weren', "werent","could","would","got","thats","ive","id","during","yet","go","us","im","said","told","must",'either',"neither","pm","mr","mrs","miss","said","went","ate","ky","later","again","now"]
    sentence=re.sub(r'[^\w\s]','', sentence)
    sentence=re.sub(r'[0-9]','',sentence)
    sentence= re.sub(r'\s+', ' ',sentence)
    sentence=sentence.lower()
    words = sentence.split(" ")
    words2=[word for word in words if word not in stopwords]
    #words2=[word for word in words2 if 
    #print(words2)
    return words2

    
    
#finds the number of words apperearing as a truthful or deceptive
#counts_dict is a dictionary of words as key and value as a dictionary with keys as truthful and deceptive and values as thier counts
def LiklihoodCounts(train_data):
    counts_dict = defaultdict(dict)
    truthful_total = 0
    deceptive_total = 0

    for i in range(len(train_data['labels'])):
        label = train_data["labels"][i]
        review = train_data["objects"][i]
        words=data_preprocessing(review)
        for word in words:
            if label == 'truthful':
                truthful_total += 1
            else:
                deceptive_total +=1
            try:
                counts_dict[word.lower()][label] += 1
            except:
                counts_dict[word.lower()][label] = 1

        '''for word,value in counts_dict.items():
            if len(value.keys())!=2:
                if 'truthful' in value.keys():
                    counts_dict[word]['truthful']+=1
                    counts_dict[word]['deceptive']=1
                else:
                    counts_dict[word]['truthful']=1
                    counts_dict[word]['deceptive']+=1'''
                    

    P_of_truthful = truthful_total/(truthful_total+deceptive_total)
    P_of_deceptive = deceptive_total/(truthful_total+deceptive_total)
    #print("counts_dict",counts_dict)
    return counts_dict,P_of_truthful,P_of_deceptive,truthful_total,deceptive_total

#finds the probability of the word given truthful and  probability of the word given deceptive
#counts_dict is a dictionary of words as key and value as a dictionary with keys as truthful and deceptive and values as thier counts
# word_probabilities is a dictionary with log probabilities of each word for each label. That is, word probabilities is a dictionary representing likelihoods
# We have used these links : https://www.kdnuggets.com/2020/07/spam-filter-python-naive-bayes-scratch.html,https://www.analyticsvidhya.com/blog/2021/04/improve-naive-bayes-text-classifier-using-laplace-smoothing/ to calculate laplace smoothing
def LiklihoodProbabilities(bag_of_words,truthful_c,deceptive_c):

    Word_Probabilities = defaultdict(dict)

    for word,data in bag_of_words.items():
        probability_deceptive = 0.1
        probability_truthful = 0.1
        alpha=0.1
        #print(data)
        if len(data.keys()) == 2:
            probability_deceptive = (data['deceptive'] + alpha)/ (deceptive_c + alpha*(deceptive_c+truthful_c))
            probability_truthful = (data['truthful'] + alpha) / (truthful_c + alpha*(deceptive_c+truthful_c))
        else:
            if 'truthful' in data.keys():
                probability_truthful = 1
            else:
                probability_deceptive = 1
        Word_Probabilities[word]['truthful'] = math.log(probability_truthful)
        Word_Probabilities[word]['deceptive'] =math.log(probability_deceptive)

    #print("word prob1",Word_Probabilities['unfortunately.'])
    #print("bag of word",bag_of_words['unfortunately.'])
    return Word_Probabilities


#This function returns the final result for the document.
#The log likelihoods are added to log prior
def NaiveBayes(truth,deceptive,P_truthful,P_deceptive):
    P_truth=truth+math.log(P_truthful)
    P_decep=deceptive+math.log(P_deceptive)
    #print(deceptive,P_deceptive)

    '''if P_decep==0:
        ratio=0
    else:'''
    
        
    if P_truth>P_decep:
        result="truthful"
        return result
    else:
        result="deceptive"
        return result


##In this function, we are adding log probabilities for all likelihoods of the document
## 
def NaivBayes1(word_probabilities,train_data,P_truthful,P_deceptive,truthful_c,deceptive_c):
    training_result=[]
    alpha=0.1
    for i in range(len(train_data["objects"])):
        
        truth=0
        deceptive=0
        sentence=train_data["objects"][i]
        parsed_words = data_preprocessing(sentence)
        #print(parsed_words)
        #print("parsed words",parsed_words)
        for word in parsed_words:
            word=word.lower()
            if 'truthful' in word_probabilities[word]:
                truth=truth+word_probabilities[word]['truthful']
            else:
                truth=truth+math.log((alpha/truthful_c+alpha*(deceptive_c+truthful_c)))
            if 'deceptive' in word_probabilities[word]:
                deceptive=deceptive+word_probabilities[word]['deceptive']
            else:
                deceptive=deceptive+math.log((alpha/deceptive_c+alpha*(deceptive_c+truthful_c)))
        
        
        result=NaiveBayes(truth,deceptive,P_truthful,P_deceptive)
        
        training_result.append(result)
    return training_result
            
        
        
        
# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#
def classifier(train_data, test_data):
    # This is just dummy code -- put yours here!
    bag_of_words, P_of_truthful,P_of_deceptive,truthful_c,deceptive_c = LiklihoodCounts(train_data)
    #print("Train Data",train_data["objects"][0])
    word_probabilities = LiklihoodProbabilities(bag_of_words,truthful_c,deceptive_c)
    
    test_result=NaivBayes1(word_probabilities,test_data,P_of_truthful,P_of_deceptive,truthful_c,deceptive_c)
    
    return test_result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    #print("Train data", train_data)

    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results= classifier(train_data, test_data_sanitized)

    #print("results len",len(results))
    #print("actual len",len(test_data["labels"]))
    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
