import operator
from collections import Counter
#------------------------------------------------------------------
#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be ---
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]

def NextWordProbability(sampletext,word):
    words = sample_memo.split()  # tokenize
    word_freq = [words[i+1] for i in range(len(words)) if words[i] == word and i < len(words)]
    result = Counter(word_freq)
    return result


def LaterWords(sample, word, distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    word_count = len(data_list)
    word_frequency = NextWordProbability(sample, word)
    probabilities = [value / float(word_count) for value in word_frequency.values()]
    p_w1_w = dict(zip(word_frequency.keys(), probabilities))
    sorted_p = sorted(p_w1_w.items(), key=operator.itemgetter(1), reverse=True)
    d1_wd = zip(*sorted_p)[0][0]

    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    for i in range(0, distance):
        print(i)
        word_frequency2 = NextWordProbability(sample, d1_wd)
        probabilities2 = [v / float(word_count) for v in word_frequency2.values()]
        p_w2_w1 = dict(zip(word_frequency2.keys(), probabilities2))
        p_w2_w1andw = dict(zip(p_w2_w1.keys(), [p_w1_w[d1_wd] * p_w2_w1[w] for w in p_w2_w1.keys()]))
        sorted_p2 = sorted(p_w2_w1andw.items(), key=operator.itemgetter(1), reverse=True)
        return zip(*sorted_p2)[0][0]




if __name__ == '__main__':
    print LaterWords(sample_memo,'gonna', 3)
