import os
import sys
sys.path.append('/Users/lihan/Documents/Magellan/magellan/')

import magellan as mg
from read_recom_list import read_wrapped_recom_list


def calc_missed_gold_not_in_recom(cmb_file_path, cand_path, gold_path, K):
    gold = mg.read_csv_metadata(gold_path)
    gold_set = set()
    for tup in gold.itertuples():
        gold_set.add((tup[1], tup[2]))

    cand_set = set()
    fin = open(cand_path, 'r')
    fin.readline()
    for line in fin:
        splits = line.split(',')
        cand_set.add((int(splits[1]), int(splits[2])))

    union_set = {}
    schema, recom_lists = read_wrapped_recom_list(cmb_file_path, K)
    for recom_list in recom_lists:
        for pair in recom_list:
            index = (int(pair[1]), int(pair[2]))
            if index not in union_set:
                union_set[index] = pair

    count = 0
    for gold_pair in gold_set:
        if gold_pair not in union_set and gold_pair not in cand_set:
            count += 1
    print count

if __name__ == "__main__":
    input_dir = '../datasets/exp_data/cleaned/'
    cand_dir = '../datasets/exp_data/candidate_sets/'
    result_dir = '../results/exp/new/'
    folder = 'Abt-Buy'
    type = 'similarity-based'
    rule = 'name_token_cos<0.4'
    K = 200
    calc_missed_gold_not_in_recom(result_dir + folder + '/' + type + '/combined_list/cmb_' + rule + '.txt',
                                  cand_dir + folder + '/' + type + '/' + rule + '.csv',
                                  input_dir + folder + '/gold.csv', K)