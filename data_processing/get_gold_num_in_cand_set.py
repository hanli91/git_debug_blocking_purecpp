import sys
sys.path.append('/Users/lihan/Documents/Magellan/magellan/')
import os
import magellan as mg


def get_gold_num_in_cand_set(gold_path, cand_path, gold_size):
    gold = mg.read_csv_metadata(gold_path)
    gold_set = set()
    for tup in gold.itertuples():
        gold_set.add((tup[1], tup[2]))

    cand = mg.read_csv_metadata(cand_path, key='_id')
    print 'raw cand set size:', len(cand)

    cand_list = list(cand.values)
    refined_cand_set = set()
    for pair in cand_list:
        if pair[1] == pair[2]:
            continue
        if (pair[2], pair[1]) in refined_cand_set:
            continue
        refined_cand_set.add((pair[1], pair[2]))

    print 'refined cand set size:', len(refined_cand_set)

    count = 0
    for tup in cand.itertuples():
        if (tup[2], tup[3]) in gold_set:
            count += 1
    print 'true matches out of C:', gold_size - count


if __name__ == "__main__":
    # input_dir = '../datasets/exp_data/cleaned/'
    # folder = 'Walmart-Amazon'
    # get_gold_num_in_cand_set(input_dir + folder + '/gold.csv',
    #                          input_dir + folder + '/candidate_sets/cand_title<0.3.csv')

    input_dir = '../datasets/exp_data/candidate_sets/'
    folder = 'Song-Song'
    type = 'rule-based'
    gold_size = 2978

    files = os.listdir(input_dir + folder + '/' + type)
    for filename in files:
        if filename == '.DS_Store':
            continue
        print filename
        get_gold_num_in_cand_set(input_dir + folder + '/gold.csv',
                             input_dir + folder + '/' + type + '/' + filename,
                             gold_size)