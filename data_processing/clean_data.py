import pandas as pd
import os


def rearrange_data(inpath, outcsvpath, outmappath, col_list, key):
    df = pd.read_csv(inpath)
    col_index_list = [tup[0] for tup in col_list]
    col_name_list = [tup[1] for tup in col_list]

    df = df[col_index_list]
    df.columns = col_name_list

    kcol = df[key]
    kcol.to_csv(outmappath, index=True, header='key', index_label='index')

    idx_col = [i for i in range(len(kcol))]
    df[key] = idx_col
    df.to_csv(outcsvpath, index=False)


def reformat_gold_set(in_csv_path, in_ltbl_map_path, in_rtbl_map_path, lkey, rkey, outpath):
    gdf = pd.read_csv(in_csv_path)
    ltdf = pd.read_csv(in_ltbl_map_path)
    rtdf = pd.read_csv(in_rtbl_map_path)
    lmap = build_key_index_map(ltdf)
    rmap = build_key_index_map(rtdf)

    lkey_col = gdf[lkey]
    rkey_col = gdf[rkey]

    for i in xrange(len(lkey_col)):
        lkey_col[i] = lmap[lkey_col[i]]
    for i in xrange(len(rkey_col)):
        rkey_col[i] = rmap[rkey_col[i]]

    gdf[lkey] = lkey_col
    gdf[rkey] = rkey_col

    gdf.columns = ['tableA_id', 'tableB_id']
    gdf.to_csv(outpath, index=False)


def build_key_index_map(df):
    idx_col = list(df['index'])
    key_col = list(df['id'])
    m = {}
    for idx, key in zip(idx_col, key_col):
        m[key] = idx
    return m


def reformat_cand_set(in_csv_path, in_ltbl_map_path, in_rtbl_map_path, lkey, rkey, outpath):
    cand_df = pd.read_csv(in_csv_path)
    ltdf = pd.read_csv(in_ltbl_map_path)
    rtdf = pd.read_csv(in_rtbl_map_path)
    lmap = build_key_index_map(ltdf)
    rmap = build_key_index_map(rtdf)

    lkey_col = cand_df[lkey]
    rkey_col = cand_df[rkey]

    for i in xrange(len(lkey_col)):
        lkey_col[i] = lmap[int(lkey_col[i])]
    for i in xrange(len(rkey_col)):
        rkey_col[i] = rmap[int(rkey_col[i])]

    cand_df[lkey] = lkey_col
    cand_df[rkey] = rkey_col

    cand_df.to_csv(outpath, index=False)


def convert_string_to_lowercase(input, output):
    f = open(input, 'r')
    out = open(output, 'w')

    for line in f:
        out.write(line.lower() + '\n')
    out.close()


def check_id(inpath):
    table = pd.read_csv(inpath)
    col = table['id']
    s = set(col)
    for i in range(len(col)):
        if i + 1 not in s:
            print i + 1

if __name__ == "__main__":
    # col_list = [(0, "id"), (1, "name"), (2, "description"), (4, "price")]
    # indir = '../datasets/exp_data/raw/Abt-Buy/'
    # outdir = '../datasets/exp_data/cleaned/Abt-Buy/'
    # csvfile = 'Buy.csv'
    # outmapfile = 'Buy_map.csv'
    # key = 'id'
    # rearrange_data(indir + csvfile, outdir + csvfile, outdir + outmapfile, col_list, key)

    # ingoldfile = 'matches_dblp_scholar.csv'
    # inltbmapfile = 'tableA_idx_key_map.csv'
    # inrtbmapfile = 'tableB_idx_key_map.csv'
    # outgoldfile = 'gold.csv'
    # reformat_gold_set(indir + ingoldfile, outdir + inltbmapfile, outdir + inrtbmapfile,
    #                   'dblp_id', 'google_scholar_id', outdir + outgoldfile)

    # indir = '../datasets/exp_data/cleaned/Walmart-Amazon/'
    # check_id(indir + 'tableB.csv')

    # col_list = [(0, "id"), (1, "name"), (2, "addr"), (3, "city"), (4, "phone"),
    #             (5, "type"), (6, "class")]
    # indir = '../datasets/exp_data/cleaned/Fodors-Zagats/'
    # outdir = '../datasets/exp_data/cleaned_for_baselines/Fodors-Zagats/'
    # csvfile = 'tableB.csv'
    # outmapfile = 'tableB_idx_key_map.csv'
    # key = 'id'
    # rearrange_data(indir + csvfile, outdir + csvfile, outdir + outmapfile, col_list, key)

    # ingoldfile = 'gold.csv'
    # inltbmapfile = 'tableA_idx_key_map.csv'
    # inrtbmapfile = 'tableB_idx_key_map.csv'
    # outgoldfile = 'gold.csv'
    # reformat_gold_set(indir + ingoldfile, outdir + inltbmapfile, outdir + inrtbmapfile,
    #                   'tableA_id', 'tableB_id', outdir + outgoldfile)
    BLOCK_TYPES = ['rule-based']
    indir = '../datasets/exp_data/candidate_sets/Song-Song/'
    outdir = '../datasets/exp_data/candidate_sets_for_baselines/Song-Song/'
    keymapdir = '../datasets/exp_data/cleaned_for_baselines/Song-Song/'
    for block_type in BLOCK_TYPES:
        rules = os.listdir(indir + block_type + '/')
        if '.DS_Store' in rules:
            rules.remove('.DS_Store')
        for rule in rules:
            print rule
            incandfile = indir + block_type + '/' + rule
            inltbmapfile = 'tableA_idx_key_map.csv'
            inrtbmapfile = 'tableB_idx_key_map.csv'
            outcandfile = outdir + block_type + '/' + rule
            reformat_cand_set(incandfile, keymapdir + inltbmapfile, keymapdir + inrtbmapfile,
                              'ltable_id', 'rtable_id', outcandfile)
