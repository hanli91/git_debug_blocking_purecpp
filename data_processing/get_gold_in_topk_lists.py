import os
import sys
sys.path.append('/Users/lihan/Documents/Magellan/magellan/')

import magellan as mg

def get_gold_in_topk_lists(topk_dir, gold_path, cmp_config_seq):
    gold = mg.read_csv_metadata(gold_path)
    gold_set = set()
    for tup in gold.itertuples():
        gold_set.add((tup[1], tup[2]))
    # print gold_set

    topk_lists = os.listdir(topk_dir)
    # print topk_lists

    catched_true_set = set()
    cmp_catched_true_set = set()
    union_set = set()
    cmp_union_set = set()

    if '.DS_Store' in topk_lists:
        topk_lists.remove('.DS_Store')
    for topk_list in topk_lists:
        selected_fields = topk_list[5:-4]

        count = 0
        fin = open(topk_dir + '/' + topk_list)
        match_list = []
        linecount = 0
        for line in fin:
            linecount += 1
            splits = line.split(' ')
            tup = (int(splits[1]) + 1, int(splits[2]) + 1)
            union_set.add(tup)
            if selected_fields in cmp_config_seq:
                cmp_union_set.add(tup)
            if tup in gold_set:
                match_list.append(linecount)
                catched_true_set.add(tup)
                if selected_fields in cmp_config_seq:
                    cmp_catched_true_set.add(tup)
                count += 1
        print topk_list + ': ' + str(count)#, match_list
    print 'total number of candidates:', len(union_set)
    print 'catched true matches:', len(catched_true_set)
    print 'candidates by cont. configs:', len(cmp_union_set)
    print 'catched true matches by cont. configs:', len(cmp_catched_true_set)

    return len(union_set), len(catched_true_set), len(cmp_union_set), len(cmp_catched_true_set)

if __name__ == "__main__":
    ### keep long field
    # KEEP_LONG_FIELD_TYPES = ['keep_long_field', 'rm_long_field']
    # BLOCK_TYPES = ['overlap', 'hash-based', 'similarity-based', 'rule-based']
    # topk = 400
    # keep_field_type = KEEP_LONG_FIELD_TYPES[1]
    # input_dir = '../datasets/exp_data/cleaned/'
    # # result_dir = '../results/exp/top' + str(topk) + '/'
    # result_dir = '../results/rm_long_field_cmp_exp/top' + str(topk) + '/' + keep_field_type + '/'
    # folder = ''
    # cmp_config_seq = ['0_1_2_3_4', '0_2_3_4', '0_2_3', '0_2', '0']
    # block_type = BLOCK_TYPES[0]
    # rules = os.listdir(result_dir + folder + '/' + block_type + '/')
    # if '.DS_Store' in rules:
    #     rules.remove('.DS_Store')
    # if 'combined_list' in rules:
    #     rules.remove('combined_list')
    # print rules
    # # rule = 'overlap/name_overlap<5'
    # union_size_list = []
    # catched_true_list = []
    # cmp_catched_true_list = []
    # for rule in rules:
    #     union_size, catched_true, cmp_catched_true = get_gold_in_topk_lists(
    #         result_dir + folder + '/' + block_type + '/' + rule, input_dir + folder + '/gold.csv', cmp_config_seq)
    #     union_size_list.append(union_size)
    #     catched_true_list.append(catched_true)
    #     cmp_catched_true_list.append(cmp_catched_true)
    # for v in rules:
    #     print v
    # for v in union_size_list:
    #     print v
    # for i in range(len(catched_true_list)):
    #     print catched_true_list[i], cmp_catched_true_list[i], cmp_catched_true_list[i] * 1.0 / catched_true_list[i]

    ### Check recall upper bound on different topk value
    # BLOCK_TYPES = ['overlap', 'hash-based', 'similarity-based', 'rule-based']
    # Walmart-Amazon
    BLOCK_TYPES = {'overlap':['title_overlap<3']}
    # BLOCK_TYPES = {'hash-based':['attr_equal_artist_name'],
    #                'rule-based':['title_token_cos<0.7_OR_year_diff'],
    #                'overlap':['artist_name_overlap<2'],
    #                'similarity-based':['title_token_cos<0.5']}
    # Amazon-GoogleProducts
    # BLOCK_TYPES = {'overlap':['title_overlap<3'],
    #                'hash-based':['attr_equal_manuf'],
    #                'similarity-based':['title_token_cos<0.4'],
    #                'rule-based':['title_jac_token<0.2_AND_manuf_jac_3gram<0.4']}
    # BLOCK_TYPES = {'rule-based': ['title_jac_token<0.2_AND_manuf_jac_3gram<0.4']}

    # ACM-DBLP
    # BLOCK_TYPES = {'overlap':['authors_overlap<2'],
    #                'similarity-based': ['title_3gram_jac<0.7'],
    #                'rule-based': ['title_token_cos<0.8_AND_authors_3gram_jac<0.8',
    #                               'title_token_jac<0.7_OR_year_absdiff>0.5']}
    # Fodors-Zagats
    # BLOCK_TYPES = {'overlap':['name_overlap<2'],
    #                'hash-based': ['attr_equal_city'],
    #                'similarity-based':['addr_3gram_jac<0.3'],
    #                'rule-based':['name_token_cos<0.5_AND_type_3gram_jac<0.7_OR_addr_3gram_jac<0.3']}
    # Song-Song
    # BLOCK_TYPES = {'overlap':['artist_name_overlap<2'],
    #                'hash-based':['attr_equal_artist_name'],
    #                'similarity-based':['title_token_cos<0.5'],
    #                'rule-based':['title_token_cos<0.7_OR_year_diff']}

    # BLOCK_TYPES = ['overlap']
    topk = 1000
    topk_type = 'new_topk_para_reuse'
    keep_long_field_type = 'rm_long_field'
    input_dir = '../../debug_blocking_cython/datasets/exp_data/cleaned/'
    result_dir = '../../debug_blocking_cython/results/final_topk_efficiency_cmp_exp/top' + str(topk) + '/new_topk_para_reuse/'
    # result_dir = '../results/exp_sensitivity_K/top' + str(topk) + '/'
    folder = 'Walmart-Amazon'
    cmp_config_seq = ['0_1_2_3_4']
    # cmp_config_seq = ['0_1_2_3', '0_1_2_4', '0_1_3_4', '1_2_3_4', '0_1_2_3_4']
    # block_type = BLOCK_TYPES[2]
    for block_type in BLOCK_TYPES:
        rules = os.listdir(result_dir + folder + '/' + block_type + '/')
        rules = BLOCK_TYPES[block_type]
        if '.DS_Store' in rules:
            rules.remove('.DS_Store')
        if 'combined_list' in rules:
            rules.remove('combined_list')
        print rules
        # rule = 'overlap/name_overlap<5'
        union_size_list = []
        catched_true_list = []
        cmp_union_size_list = []
        cmp_catched_true_list = []
        for rule in rules:
            print '\n', rule
            union_size, catched_true, cmp_union_size, cmp_catched_true, = get_gold_in_topk_lists(
                result_dir + folder + '/' + block_type + '/' + rule, input_dir + folder + '/gold.csv', cmp_config_seq)
            union_size_list.append(union_size)
            cmp_union_size_list.append(cmp_union_size)
            catched_true_list.append(catched_true)
            cmp_catched_true_list.append(cmp_catched_true)
        for v in rules:
            print v
        # for v in union_size_list:
        #     print v
        # for i in range(len(union_size_list)):
        #     print union_size_list[i], cmp_union_size_list[i]#, cmp_union_size_list[i] * 1.0 / union_size_list[i]
        for i in range(len(catched_true_list)):
            print catched_true_list[i], cmp_catched_true_list[i]#, cmp_catched_true_list[i] * 1.0 / catched_true_list[i]
        # for i in range(len(union_size_list)):
        #     print union_size_list[i], catched_true_list[i]
