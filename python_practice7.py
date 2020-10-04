# SEARCH ENGINE #
"""The task you have to perform is “Search Engine”. This task consists of a total of 20 points to evaluate your performance.

Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance
after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the
 maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

1. python is not python snake
2. python is good
3. Python is cool"""
"""
def mathing_words(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0

    ##### for logic of score print ####
    for word1 in words1:
        for word2 in words2:
            #print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    sentences = ["python is cool", "python is good", "python is not python snake"]
    query = input("Please input the query string : \n")
    scores = [mathing_words(query, sentence) for sentence in sentences]
    #print(scores)

    ############ print for ascending order of most common matched ##################################
    sorted_senten_score = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True) if sentscore[0] !=0]
    #print(sorted_senten_score)

    ### for total no. of results ##
    print(f"{len(sorted_senten_score)} results found!")


    for score, item in sorted_senten_score:
        print(f"{item} : with a score of {score}")"""

###############################################################################################################
###############################################################################################################
###############################################################################################################

def mathing_words(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score = score +1
    return score

if __name__ == '__main__':
    sentences = ["python is cool", "python is good", "python is not python snake"]
    query = input("Enter here for queries : ")

    score = [mathing_words(query, sentence) for sentence in sentences]

    sent_score = [sent_score  for sent_score in sorted(zip(score, sentences), reverse = True) if sent_score[0] != 0]

    #print(f"{len(sorted_senten_score)} results found!")
    print(f"{len(sent_score)} result found !")

    for score, item in sent_score:
        #print(f"{item} : is matching with score {score}")
        print(item)




