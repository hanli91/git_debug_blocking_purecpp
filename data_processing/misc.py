import sys

sys.path.append('/Users/lihan/Documents/Magellan/magellan/')

import magellan as mg
import magellan.catalog.catalog_manager as cm
import pandas as pd
import numpy as np

if __name__ == "__main__":
    start = 186
    for i in range(15):
        print '=recall(' + 'H' + str(start + i) + ', ' + 'F' + str(start + i) + ', ' + 'D' + str(start + i) + ')'

    # inpath = '../datasets/exp_data/cleaned/Song-Song/gold_full.csv'
    # outpath = '../datasets/exp_data/cleaned/Song-Song/gold.csv'
    # gold = pd.read_csv(inpath)
    #
    # gold = gold[gold.tableA_id <= 100000]
    # gold = gold[gold.tableB_id <= 100000]
    # gold = gold[gold.tableA_id != gold.tableB_id]
    # print len(gold)
    #
    # gold.to_csv(outpath, index=False)

    # candpath = '../datasets/exp_data/candidate_sets/Song-Song/rule-based/title_token_cos<0.7_OR_year_diff_raw.csv'
    # outpath = '../datasets/exp_data/candidate_sets/Song-Song/rule-based/title_token_cos<0.7_OR_year_diff.csv'
    # cand = pd.read_csv(candpath)
    # cand_list = list(cand.values)
    # length = 0
    # for pair in cand_list:
    #     length = max(length, pair[0])
    # length += 1
    # for i in range(100000):
    #     cand_list.append(np.array([length + i, i + 1, i + 1]))
    #
    # cand_df = pd.DataFrame(cand_list)
    # cand_df.columns = cand.columns
    # cand_df.to_csv(outpath, index=False)

    # inpath = '../datasets/exp_data/cleaned/Song-Song/tableA_full.csv'
    # outpath = '../datasets/exp_data/cleaned/Song-Song/tableA.csv'
    # ltable = mg.read_csv_metadata(inpath, key='id')
    # ltable = ltable[0:100000]
    # mg.to_csv_metadata(ltable, outpath)

