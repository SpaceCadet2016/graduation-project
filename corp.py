import sys
from nltk.corpus import gutenberg
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk
from nltk.probability import FreqDist
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from codecs import open
from nltk import FreqDist
from nltk.corpus import gutenberg
from nltk.collocations import *
import matplotlib
import matplotlib.pyplot as plt

class gutenberg_corp:
    def __init__(self,corpname):
        self.text=nltk.Text(nltk.corpus.gutenberg.words(corpname))
        self.sents=gutenberg.sents(corpname)
        self.raw=gutenberg.raw(corpname)
        self.words=gutenberg.words(corpname)

    def longest_sent(self):
        longest_len = max(len(s) for s in self.sents)
        return[s for s in self.sents if len(s) == longest_len]

    def ins_sent(self, numb):
        return self.sents[numb]

    def giving_len_sent(self, slen):
        return[s for s in self.sents if len(s) == slen]

    def div(self): #diversity
        return len(set(self.raw)) / len(self.raw)

    def perc(self, word): #percentage
        return 100 * self.text.count(word) / len(self.text)

    def concordance(self, word):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.text.concordance(word)
        sys.stdout = old_stdout
        return mystdout.getvalue()

    def collocations(self):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.text.collocations()
        sys.stdout = old_stdout
        return mystdout.getvalue()

    def similar(self, word):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.text.similar(word)
        sys.stdout = old_stdout
        return mystdout.getvalue()

    def common_contexts(self, words):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.text.common_contexts(words)
        sys.stdout = old_stdout
        return mystdout.getvalue()

    def least_common(self):
        return(FreqDist(self.text).hapaxes())

    def word_count(self,word):
        return(self.text.count(word))

    def get_max_word_len(self):
        return max([len(w) for w in set(self.words)])

    def get_words_with_given_len(self, wlen):
        return [w for w in set(self.text) if len(w) == wlen]

    def get_words_with_max_len(self):
        return self.get_words_with_given_len(self.get_max_word_len())

    def __levenshtein(self,s1, s2):
        if len(s1) < len(s2):
            tmp=s1
            s1=s2
            s2=tmp
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1 
                deletions = current_row[j] + 1      
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
    
        return previous_row[-1]

    def similar_words(self, word, count):
        result = []
        r = re.compile('[A-Za-z0-9]+')
        for w in self.words:
            if r.match(w):
                if self.__levenshtein(word, w) <= count:
                    if not w in result:
                        result.append(w)
        return result

    def statistics(self):
        result = {}
        result['chars'] = len(self.raw)
        result['words'] = len(self.words)
        result['sents'] = len(self.sents)
        result['vocab'] = len(set([w.lower() for w in self.words]))
        result['avg_word'] = int(result['chars'] // result['words'])
        result['avg_sent'] = int(result['words'] // result['sents'])
        result['avg_vocab'] = int(result['words'] // result['vocab'])
        return result

    def plot_len_words(self):
        [len(w) for w in self.text]
        D= fdist = FreqDist(len(w) for w in self.text)
        plt.bar(range(len(D)), D.values(), align='center')
        plt.xticks(range(len(D)), D.keys())
        plt.autoscale(tight=True)
        plt.xlabel(u'Количество букв в слове', family="Verdana", fontsize=14)
        plt.ylabel(u'Количество слов', family="Verdana", fontsize=14)
        plt.title(u'Длина слов', family="Verdana", color="blue", fontsize=20)
        plt.grid()
        plt.show()
    
    def plot_len_sents(self):
        [len(w) for w in self.sents]
        D= fdist = FreqDist(len(w) for w in self.sents)
        plt.bar(range(len(D)), D.values(), align='center')
        plt.xticks(range(len(D)), D.keys())
        plt.autoscale(tight=True)
        plt.xlabel(u'Количество слов в предложении', family="Verdana", fontsize=14)
        plt.ylabel(u'Количество предложений', family="Verdana", fontsize=14)
        plt.title(u'Длина предложений в словах', family="Verdana", color="blue", fontsize=20)
        plt.grid()
        plt.show()

    def all_words(self):
        fdist=FreqDist(self.text)
        return fdist.most_common()
    
    def plot_words(self):
        fdist=FreqDist(self.text)

        return fdist.plot(100,cumulative=False)

    def disp_plot(self, words):
        return self.text.dispersion_plot(words)


