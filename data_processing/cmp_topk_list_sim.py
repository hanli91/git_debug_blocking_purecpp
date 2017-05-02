import os

def compare_topk_list_sim(file1, file2):
    fin1 = open(file1, 'r')
    fin2 = open(file2, 'r')

    set1 = set()
    set2 = set()
    for line in fin1:
        splits = line.strip().split(' ')
        set1.add((splits[1], splits[2]))

    for line in fin2:
        splits = line.strip().split(' ')
        set2.add((splits[1], splits[2]))

    print len(set1 & set2)

if __name__ == "__main__":
    topk = 1000
    BLOCK_TYPES = ['overlap', 'hash-based', 'similarity-based', 'rule-based']
    block_type = BLOCK_TYPES[0]
    folder = 'Walmart-Amazon'
    indir = '../results/rm_long_field_cmp_exp/top' + str(topk) + '/keep_long_field/' + folder + '/' + block_type + '/'
    rules = os.listdir(indir)
    if '.DS_Store' in rules:
        rules.remove('.DS_Store')
    if 'combined_list' in rules:
        rules.remove('combined_list')
    print rules
    for rule in rules:
        file1 = indir + rule + '/topk_0_1_2_3.txt'
        file2 = indir + rule + '/topk_0_2_3.txt'
        compare_topk_list_sim(file1, file2)