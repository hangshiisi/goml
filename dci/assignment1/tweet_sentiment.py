import sys
import json 


def lines_in(f):
    '''parse sentiment file, returns dictionary''' 
    scores = {} 
    with open(f) as fp: 
        for line in fp: 
            term, score = line.split("\t") 
            scores[term] = int(score) 
        return scores 

def tweet_score(tweet, scores): 
    '''returns the score for a tweet or 0 if it's not in file''' 
    return sum(scores.get(word, 0) for word in tweet.split())    

def lines_out(f, scores):
    '''Calculate scores for all tweets in tweet file'''
    with open(f) as fp:  
        tweets = (json.loads(line).get('text','') for line in fp) 
        return [tweet_score(tweet, scores) for tweet in tweets]  


def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = lines_in(sent_file)
    senti_scores = lines_out(tweet_file, scores)
    print(senti_scores) 
    sys.stdout.writelines('{0}.0\n'.format(score) for score in senti_scores) 


if __name__ == '__main__':
    main()
