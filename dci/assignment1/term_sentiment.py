from __future__ import division
import sys
import json


def read_scores(sent_file):
    '''parse sentiment file, returns dictionary''' 
    scores = {} 
    with open(sent_file) as fp: 
        for line in fp: 
            term, score = line.split("\t") 
            scores[term] = int(score) 
        return scores 

def score_tweet(tweet, scores):
    '''returns the score for a tweet or 0 if it's not in file''' 
    return sum(scores.get(word, 0) for word in tweet)


def unknown_word_scores(tweet_file, scores):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return {word: score_tweet(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores}

def main(): 
    scores = read_scores(sent_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in unknown_word_scores(
                              tweet_file=sys.argv[2],
                              scores=scores).items())


if __name__ == '__main__':
    main()

