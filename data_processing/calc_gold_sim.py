import sys
sys.path.append('/Users/lihan/Documents/Magellan/magellan/')

import magellan as mg
import numpy as np
import pandas as pd


def calc_recom_not_in_gold_sim(recom_path, gold_path, ltable_path, rtable_path, lkey, rkey, fields):
    fin = open(recom_path, 'r')
    lines = fin.readlines()
    recom_list = []
    for line in lines:
        splits = line.split(' ')
        recom_list.append((splits[0], int(splits[1]), int(splits[2])))

    ltable = mg.read_csv_metadata(ltable_path, key=lkey)
    rtable = mg.read_csv_metadata(rtable_path, key=rkey)
    gold = mg.read_csv_metadata(gold_path)
    gold_set = set()
    for tup in gold.itertuples():
        gold_set.add((tup[1], tup[2]))

    sim_list = []
    for tuple in recom_list:
        if (tuple[1], tuple[2]) not in gold_set:
            lrec = list(ltable.ix[tuple[1]])
            rrec = list(rtable.ix[tuple[2]])
            lset = tokenize(lrec, fields)
            rset = tokenize(rrec, fields)
            sim_list.append((tuple[1], tuple[2], tuple[0], len(lset & rset) * 1.0 / len(lset | rset)))
    sim_list = sorted(sim_list, key=lambda x:x[2], reverse=True)
    cols = ltable.columns

    for i in range(len(sim_list)):
        tuple = sim_list[i]
        print '=====rank ' + str(i + 1) + '====='
        print 'pair:(' + str(tuple[0]) + ', ' + str(tuple[1]) + ')'
        print 'topk sim:', tuple[2]
        print 'new calc sim:', tuple[3]
        lrec = list(ltable.ix[int(tuple[0])])
        rrec = list(rtable.ix[int(tuple[1])])
        for value in fields:
            print cols[value] + ':', '<left>' + str(lrec[value]) + '\t<right>' + str(rrec[value])
        print '\n'

    return


def calc_gold_sim(gold_path, ltable_path, rtable_path, lkey, rkey, fields):
    ltable = mg.read_csv_metadata(ltable_path, key=lkey)
    rtable = mg.read_csv_metadata(rtable_path, key=rkey)
    gold = mg.read_csv_metadata(gold_path)
    sim_list = []
    for tuple in gold.itertuples():
        lrec = list(ltable.ix[int(tuple[1])])
        rrec = list(rtable.ix[int(tuple[2])])
        lset = tokenize(lrec, fields)
        rset = tokenize(rrec, fields)
        sim_list.append((tuple[1], tuple[2], len(lset & rset) * 1.0 / len(lset | rset)))
    sim_list = sorted(sim_list, key=lambda x:x[2], reverse=True)
    cols = ltable.columns

    for i in range(len(sim_list)):
        tuple = sim_list[i]
        print '=====rank ' + str(i + 1) + '====='
        print 'pair:(' + str(tuple[0]) + ', ' + str(tuple[1]) + ')'
        print 'sim:', tuple[2]
        lrec = list(ltable.ix[int(tuple[0])])
        rrec = list(rtable.ix[int(tuple[1])])
        for value in fields:
            print cols[value] + ':', '<left>' + str(lrec[value]) + '\t<right>' + str(rrec[value])
        print '\n'

    return


def tokenize(record, fields):
    catstr = ''
    for i in fields:
        if not pd.isnull(record[i]):
            catstr += ' ' + str(record[i])

    tokens = catstr.split(' ')
    if '' in tokens:
        tokens.remove('')

    tok_list = []
    tok_map = {}
    for tok in tokens:
        if tok in tok_map:
            tok_list.append(tok + '_' + str(tok_map[tok]))
            tok_map[tok] += 1
        else:
            tok_list.append(tok)
            tok_map[tok] = 1

    return set(tok_list)


if __name__ == "__main__":
    input_dir = '../datasets/exp_data/cleaned/'
    recom_dir = '../results/exp/'
    folder = 'Abt-Buy'
    rule = 'cand_title<0.7'
    file = 'topk_0_1_2.txt'
    lkey = 'id'
    rkey = 'id'
    fields = [0, 1, 2]
    # calc_gold_sim(input_dir + '/' + folder + '/gold.csv',
    #               input_dir + '/' + folder + '/tableA.csv',
    #               input_dir + '/' + folder + '/tableB.csv', lkey, rkey, fields)
    calc_recom_not_in_gold_sim(recom_dir + folder + '/' + rule + '/' + file, input_dir + '/' + folder + '/gold.csv',
                  input_dir + '/' + folder + '/tableA.csv',
                  input_dir + '/' + folder + '/tableB.csv', lkey, rkey, fields)
    pass