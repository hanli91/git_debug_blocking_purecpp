import os

def compare_recom_list(file1, file2):
    fin1 = open(file1, 'r')
    fin2 = open(file2, 'r')

    lines1 = fin1.readlines()
    lines2 = fin2.readlines()

    set1 = {}
    set2 = {}
    for line in lines1:
        splits = line.strip().split(' ')
        value = float(splits[0])
        if value in set1:
            set1[value] += 1
        else:
            set1[value] = 1

    for line in lines2:
        splits = line.strip().split(' ')
        value = float(splits[0])
        if value in set2:
            set2[value] += 1
        else:
            set2[value] = 1

    lcount = 0
    for v1 in set1:
        for v2 in set2:
            if abs(v1 - v2) <= 1e-6:
                lcount += 1
    if lcount != len(set1):
        print 'set1 value not in set2:', file1
        return

    rcount = 0
    for v2 in set2:
        for v1 in set1:
            if abs(v1 - v2) <= 1e-6:
                rcount += 1
    if rcount != len(set2):
        print 'set2 value not in set1:', file2
        return

    for v1 in set1:
        if set1[v1] != set2[v1]:
            print 'set1 and set2 have diff. number for:', v1, file1
            return


def compare_recom_lists(dir1, dir2):
    files = os.listdir(dir2)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    if 'combined_list' in files:
        files.remove('combined_list')

    # file_count = 0
    # for file in files:
    #     rule_dir1 = dir1 + file + '/'
    #     rule_dir2 = dir2 + file + '/'
    #     topk_files = os.listdir(rule_dir1)
    #     if '.DS_Store' in topk_files:
    #         topk_files.remove('.DS_Store')
    #     for topk_file in topk_files:
    #         compare_recom_list(rule_dir1 + topk_file, rule_dir2 + topk_file)
    #         file_count += 1
    file_count = 0
    for file in files:
        compare_recom_list(dir1 + file, dir2 + file)
        file_count += 1
    print file_count


if __name__ == "__main__":
    # BLOCK_TYPES = ['overlap', 'hash-based', 'similarity-based', 'rule-based']
    # BLOCK_TYPES = ['hash-based']
    # BLOCK_TYPES = {'overlap':'title_overlap<3',
    #                'hash-based':'attr_equal_brand',
    #                'similarity-based':'title_token_cos<0.4',
    #                'rule-based':'title_token_jac<0.5_OR_absdiff_price>20'}
    BLOCK_TYPES = {'overlap':'title_overlap<3',
                   'hash-based':'attr_equal_manuf',
                   'similarity-based':'title_token_cos<0.4',
                   'rule-based':'title_jac_token<0.2_AND_manuf_jac_3gram<0.4'}
    topk = 1000
    # topk_dir1 = '../../debug_blocking_cython/results/exp/top' + str(topk) + '/'
    topk_dir1 = '../results/exp_reuse_topk/top' + str(topk) + '/'
    topk_dir2 = '../results/exp_long_field/top' + str(topk) + '/'
    # topk_dir2 = '../'
    folder = 'Amazon-GoogleProducts'
    for block_type in BLOCK_TYPES:
        dir1 = topk_dir1 + folder + '/' + block_type + '/' + BLOCK_TYPES[block_type] + '/'
        # dir1 = topk_dir2 + type1 + '/' + folder + '/' + block_type + '/'
        dir2 = topk_dir2 + folder + '/' + block_type + '/' + BLOCK_TYPES[block_type] + '/'
        compare_recom_lists(dir1, dir2)
