
from nltk.util import pad_sequence
from nltk.util import bigrams
from collections import Counter
from itertools import dropwhile


poets_list = ['ferdosi','hafez','molavi']

#add start and end charachters to one line
def pading(line,start,end):
    line = line.rstrip().replace('\u200c','').split(" ")
    line = list(pad_sequence(line,
            pad_left=True, left_pad_symbol=start,
            pad_right=True, right_pad_symbol=end,
            n=2))
    return line

def calculuse_ngarams_probability(file_name):
    all_sentences = []
    all_bigrams = []
    few_occurrences_words = []
    bigram_language_model={}
    unigram_langua_model = {}
    wordDict = Counter()
    bigramsDict = Counter()
    allWords_num = 0


    with open(file_name,'r',encoding='utf-8') as f:
        for line in f:
            line = pading(line,"<s>","</s>")
            all_sentences.append(line)
    
    for line in all_sentences:
        wordDict.update(line)
    
    #if you want to remove the few_occurrences_words add the below comments to your code


    # occurence_lower_thershold = 2
    # for word in wordDict.items():
    #     if word[1] < occurence_lower_thershold:
    #         few_occurrences_words.append(word[0])


    # for key, count in dropwhile(lambda key_count: key_count[1] >= occurence_lower_thershold, wordDict.most_common()):
    #     del wordDict[key]
    
    # for line in all_sentences:
    #     for word in few_occurrences_words :
    #         # for x in range(line.count(word)):
    #         if word in line:
    #             line.remove(word)
    #     allWords_num += len(line)
    

    for line in all_sentences:
        all_bigrams.append(list(bigrams(line)))

    

    for line in all_bigrams:
        bigramsDict.update(line)

    print(" bigram and wordCount dictionary created for {}".format(file_name[:-4]))
    
    

    wordCount_name = "wordCount" +file_name 
    with open(wordCount_name,'w',encoding='utf-8') as f:
        for word, count in wordDict.most_common():
            f.write("{} : {} \n".format(word,count))


    bigrams_name ="bigrams"+file_name
    with open(bigrams_name,'w',encoding='utf-8') as f:
        for word, count in bigramsDict.most_common():
            f.write("{} : {} \n".format(word,count))

    
    
    for item in bigramsDict.items():
        bigram_language_model[item[0]] = item[1] / wordDict[item[0][0]]
    print("language_model_bigram dict created")

    prob_bigrams_name ="prob_bigrams"+file_name
    with open(prob_bigrams_name,'w',encoding='utf-8') as f:
        for word, count in bigram_language_model.items():
            f.write("{} : {} \n".format(word,count))
    
    for x in wordDict.items():
        allWords_num += x[1]
    
    for item in wordDict.items():
        unigram_langua_model[item[0]] = item[1]/allWords_num

    print("language_model_unigram dict created")
    print("".center(40,"*"))
    
    return bigram_language_model,unigram_langua_model



def probability_calculator(bigram,unigram, y1,y2,y3,e):
    return ((bigram*y3) + (unigram*y2) + (e*y1))
    

def poet_probability(poet_bigram,poet_unigram,sentence,y1,y2,y3,e):
    probability  = 1
    bigram_list = list(bigrams(sentence))
    for bigram in bigram_list :
        x = probability_calculator(poet_bigram.get(bigram,0),poet_unigram.get(bigram[1],0),y1,y2,y3,e)
        probability *=x
    return(probability)


def chose_poet(sentence,p_prob1,p_prob2,p_prob3,y1,y2,y3,e):
    plist = []
    plist.append( p_prob1 * (poet_probability(fer_bigramDict,fer_unigramDict,sentence,y1,y2,y3,e)))
    plist.append( p_prob2 * (poet_probability(haf_bigramDict,haf_unigramDict,sentence,y1,y2,y3,e)))
    plist.append( p_prob3 * (poet_probability(molav_bigramDict,molav_unigramDict,sentence,y1,y2,y3,e)))
    
    return(plist.index(max(plist))+1)


def accuracy(test_file,p_prob1,p_prob2,p_prob3,y1,y2,y3,e):
    print("for y1 = {}, y2 = {}, y3 = {}, e = {} ".format(y1,y2,y3,e))
    accuracy = 0
    line_num = 0
    chosen_poets = []
    fasle = []
    with open(test_file,'r',encoding='utf-8') as f:
        for line in f :
            line_num +=1
            poet ,sentence = line.split("\t")
            sentence = pading(sentence,"<s>","</s>")
            t =chose_poet(sentence,p_prob1,p_prob2,p_prob3,y1,y2,y3,e)
            chosen_poets.append(poets_list[t-1])
            if int(poet) == t :
                accuracy +=1
            else:
                fasle.append(line_num)
    
    print("accuracy: ",accuracy/line_num)
    print(Counter(chosen_poets))
    print("number of wrong answers: ",len(fasle))
    print("".center(40,"*"))

fer_bigramDict,fer_unigramDict = calculuse_ngarams_probability("ferdowsi_train.txt")
haf_bigramDict,haf_unigramDict = calculuse_ngarams_probability("hafez_train.txt")
molav_bigramDict,molav_unigramDict = calculuse_ngarams_probability("molavi_train.txt")

while True :
    y1,y2,y3,e = map(float,input("please enter y1,y2,y3,e in order: ").split(" "))
    accuracy("test_file.txt",(1/3),(1/3),(1/3),y1,y2,y3,e)



