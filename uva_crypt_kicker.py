# In Obedience to the Truth

# UVa 843


# WA

import collections
import itertools


def is_valid(words, dic, table):
    transtable = str.maketrans(dict(table))
    if all(w.translate(transtable) in dic[(len(w), len(set(w)))]
           for w in subset for subset in words):
        print({w.translate(transtable) for w in subset for subset in words})
        return True
    print('check failed')
    return False


def build_table(words, dic, table):

    def match_words(w, d):
        print('        match_words: {}, {}'.format(w, d))
        nonlocal table
        word_table = collections.defaultdict(lambda:None)
        for i, l in enumerate(w):
            if table[l] is None:
                word_table[l] = d[i]
            elif table[l] != d[i]:
                # Words don't match
                print('       words do not match')
                return False
        print('       words match {}'.format(word_table))
        return word_table

    def equal_subset_match(ws, ds):
        print('    equal_subset_match: {} {}'.format(ws, ds))
        nonlocal table
        for w, d in zip(ws, ds):
            match = match_words(w, d)
            if not match:
                return None
            table.update(match)
            return True

    def partition_match(ws, ds):
        print()
        print('partition_match: {}, {}'.format(ws, ds))
        nonlocal table, pindex

        words = list(ws)
        for dperm in itertools.permutations(ds, len(words)):
            dlist = list(dperm)
            table_bak = table.copy() # backup the current `table` status
            pindex += 1
            match =  equal_subset_match(words, dlist)
            if match is None:
                print('match is None')
                table = table_bak # restore the previous `table` status
                pindex -= 1
                continue
            print('incremented pindex {}'.format(pindex))
            if partition_match(words[partitions_index[pindex]],
                               dic[partitions_index[pindex]]):
                if is_valid(words, dic, table):
                    return True

            table = table_bak # restore the previous `table` status
            pindex -= 1

        # couldn't find any matching arrangement of the words
        return None


    # sorted to work on longer words first
    partitions_index = list(sorted(words.keys()))
    print(partitions_index)
    pindex = 0
    if partition_match(words[partitions_index[pindex]],
                       dic[partitions_index[pindex]]):
        return true
    else:
        return None


if __name__ == '__main__':
    # container for words in sentence and dictionnary on their length
    # the number of distinct characters
    words = collections.defaultdict(set)
    dic = collections.defaultdict(set)

    # translation table for each character in the sentence
    table = collections.defaultdict(lambda:None)

    nwords = int(input())

    dic.clear()
    for _ in range(nwords):
        word = input()
        dic[(len(word), len(set(word)))] |= { word }

    print(dic)

    while True:
        words.clear()
        table.clear()
        try:
            sentence = input()
            # number of distinct characters in sentence except ' '
            NCHARS = len(set(sentence) - {' '})
            sentence = sentence.split()
        except EOFError:
            break

        for word in sentence:
            words[(len(word), len(set(word)))] |= { word }
            for c in word:
                table[c] = None

        print(words)
        input()

        build_table(words, dic, table)

        if len(table) == 0 :
            # translation failed
            print(' '.join(['*' * len(word) for word in sentence]))
            continue

        transtable = str.maketrans(dict(table))
        print(' '.join([word.translate(transtable) for word in sentence]))



