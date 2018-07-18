from collections import Counter,OrderedDict
import operator

if __name__ == '__main__':

    countWords = Counter(list(input()))
    d_view = [(v, k) for k, v in countWords.items()]

    # d_view.sort(reverse=True)
    d_view.sort(key=operator.itemgetter(1))
    d_view.sort(key=operator.itemgetter(0), reverse=True)
    for v, k in d_view[:3]:
        print("%s %d" % (k, v))
