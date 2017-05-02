from os import listdir
from os.path import isfile
import sys
import numpy as np
import collections
sys.path.append('/Users/lihan/Documents/Magellan/magellan/')

import magellan as mg


def combine_recom_lists(indir_path, outpath, ltable_path, rtable_path, field_corres, lkey, rkey):
    ltable = mg.read_csv_metadata(ltable_path, key=lkey)
    rtable = mg.read_csv_metadata(rtable_path, key=rkey)
    filenames = [f for f in listdir(indir_path) if f.endswith('.txt')]
    out = open(outpath, 'w')
    # columns = ltable.columns
    # out.write('@_@_@_@'.join(columns) + '\n')
    schema = [tup[0] for tup in field_corres]
    out.write('@_@_@_@'.join(schema) + '\n')
    # field_corres.remove((lkey, rkey))
    print filenames

    for filename in filenames:
        fin = open(indir_path + filename)
        lines = fin.readlines()
        out.write(str(len(lines)) + '\n')
        recom_map = {}
        for line in lines:
            splits = line.strip().split(' ')
            sim = float(splits[0])
            if sim in recom_map:
                recom_map[sim].append((splits[1], splits[2]))
            else:
                recom_map[sim] = [(splits[1], splits[2])]
        od = collections.OrderedDict(sorted(recom_map.items(), reverse=True))
        print od

        rank = 1
        for sim in od:
            items = od[sim]
            for item in items:
                lrec = ltable.iloc[int(item[0])]
                rrec = rtable.iloc[int(item[1])]
                out.write(str(rank) + '\n' + str(lrec[lkey]) + '\n' + str(rrec[rkey]) + '\n')
                for tup in field_corres:
                    out.write(str(lrec[tup[0]]).replace('\n', '') + '\n')
                for tup in field_corres:
                    out.write(str(rrec[tup[1]]).replace('\n', '') + '\n')
            rank += len(items)
    out.close()


if __name__ == "__main__":
    # # folder = 'Abt-Buy'
    # # rule = 'cand_title<0.6'
    # # folder = 'Amazon-GoogleProducts'
    # # rule = 'cand_title_token<0.6_AND_manuf_3gram<0.6'
    # # folder = 'citations'
    # # rule = 'cand_rule8'
    # # folder = 'DBLP-ACM'
    # # rule = 'cand_title_token_jac<0.8_AND_venue_3gram_jac<0.5'
    # folder = 'restaurants'
    # rule = 'cand_name_token_jac<0.5_AND_type_token_jac<0.5'
    # ltable_path = '../datasets/exp_data/cleaned/' + folder + '/tableA.csv'
    # rtable_path = '../datasets/exp_data/cleaned/' + folder + '/tableB.csv'
    # indir_path = '../results/exp/' + folder + '/' + rule + '/'
    # outpath = '../results/exp/' + folder + '/combined_list/cmb_' + rule + '.txt'
    # combine_recom_lists(indir_path, outpath, ltable_path, rtable_path, 'id', 'id')

    # folder = 'L_bsarkar'
    # ltable_path = '../datasets/' + folder + '/tableA.csv'
    # rtable_path = '../datasets/' + folder + '/tableB.csv'
    # indir_path = '../results/new_allconfig_reuse_openmp/' + folder + '/'
    # outpath = '../results/new_allconfig_reuse_openmp/' + folder + '/combined_list/combined_list.txt'
    # field_corres = [('Id', 'Id'), ('Name', 'Name'), ('Director', 'Director'),
    #                 ('Creator', 'Creator'), ('Cast', 'Cast'), ('Duration', 'Duration'),
    #                 ('RatingValue', 'RatingValue'), ('Genre', 'Genre'),
    #                 ('Description', 'Description')]
    # combine_recom_lists(indir_path, outpath, ltable_path, rtable_path, field_corres, 'Id', 'Id')

    # folder = 'M_ganz'
    # ltable_path = '../datasets/' + folder + '/tableA.csv'
    # rtable_path = '../datasets/' + folder + '/tableB.csv'
    # indir_path = '../results/new_allconfig_reuse_openmp/' + folder + '/'
    # outpath = '../results/new_allconfig_reuse_openmp/' + folder + '/combined_list/combined_list.txt'
    # field_corres = [('id', 'id'), ('Title', 'Title'), ('Year', 'Year'),
    #                 ('Rating', 'Rating'), ('Director', 'Director'), ('Creators', 'Creators'),
    #                 ('Cast', 'Cast'), ('Genre', 'Genre'), ('Duration', 'Duration'),
    #                 ('ContentRating', 'ContentRating'), ('Summary', 'Summary')]
    #
    # combine_recom_lists(indir_path, outpath, ltable_path, rtable_path, field_corres, 'id', 'id')

    # folder = 'ebooks'
    # ltable_path = '../datasets/' + folder + '/A.csv'
    # rtable_path = '../datasets/' + folder + '/B.csv'
    # indir_path = '../results/new_allconfig_reuse_openmp/' + folder + '/'
    # outpath = '../results/new_allconfig_reuse_openmp/' + folder + '/combined_list/combined_list.txt'
    # field_corres = [('record_id', 'record_id'), ('publisher', 'publisher'), ('date', 'date'),
    #                 ('description', 'description'), ('title', 'title'), ('author', 'author'),
    #                 ('short_description', 'short_description')]
    # combine_recom_lists(indir_path, outpath, ltable_path, rtable_path, field_corres, 'record_id', 'record_id')

    # folder = 'Abt-Buy'
    # rule = 'cand_title<0.6'
    # folder = 'Amazon-GoogleProducts'
    # rule = 'cand_title_token<0.6_AND_manuf_3gram<0.6'
    # folder = 'citations'
    # rule = 'cand_rule8'
    # folder = 'DBLP-ACM'
    # rule = 'cand_title_token_jac<0.8_AND_venue_3gram_jac<0.5'
    # folder = 'restaurants'
    # rule = 'cand_name_token_jac<0.5_AND_type_token_jac<0.5'

    # For Abt-Buy
    # field_corres = [('id', 'id'), ('name', 'name'), ('description', 'description'), ('price', 'price')]

    # For Amazon-GoogleProducts
    # field_corres = [('id', 'id'), ('title', 'title'), ('description', 'description'),
    #                 ('manufacturer', 'manufacturer'), ('price', 'price')]

    # For Walmart-Amazon
    # field_corres = [('id', 'id'), ('title', 'title'), ('category', 'category'),
    #                 ('brand', 'brand'), ('modelno', 'modelno'), ('price', 'price'),
    #                 ('proddescrlong', 'proddescrlong')]

    # For ACM-DBLP
    # field_corres = [('id', 'id'), ('title', 'title'), ('authors', 'authors'),
    #                 ('venue', 'venue'), ('year', 'year')]

    # For Fodors-Zagats
    # field_corres = [('id', 'id'), ('name', 'name'), ('addr', 'addr'), ('city', 'city'),
    #                 ('phone', 'phone'), ('type', 'type'), ('class', 'class')]

    # For Song-Song
    # field_corres = [('id', 'id'), ('title', 'title'), ('release', 'release'), ('artist_name', 'artist_name'),
    #                 ('duration', 'duration'), ('artist_familiarity', 'artist_familiarity'),
    #                 ('artist_hotttnesss', 'artist_hotttnesss'), ('year', 'year')]
    BLOCK_TYPES = ['overlap', 'hash-based', 'similarity-based', 'rule-based']
    # BLOCK_TYPES = ['rule-based']
    # topk = 1500
    # TOPK_LIST = [1, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
    TOPK_LIST = [1000]
    for topk in TOPK_LIST:
        folder = 'Amazon-GoogleProducts'
        # block_type = BLOCK_TYPES[3]
        # rule = 'title_token_jac<0.6_OR_absdiff_price>10'
        # rules = listdir('../results/exp/top' + str(topk) + '/' + folder + '/' + block_type + '/')
        for block_type in BLOCK_TYPES:
            rules = listdir('../results/exp/top' + str(topk) +
                            '/' + folder + '/' + block_type + '/')
            if '.DS_Store' in rules:
                rules.remove('.DS_Store')
            if 'combined_list' in rules:
                rules.remove('combined_list')
            print rules
            for rule in rules:
                ltable_path = '../datasets/exp_data/cleaned/' + folder + '/tableA.csv'
                rtable_path = '../datasets/exp_data/cleaned/' + folder + '/tableB.csv'
                # indir_path = '../results/exp/top' + str(topk) + '/' + folder + '/' + block_type + '/' + rule + '/'
                # outpath = '../results/exp/top' + str(topk) + '/' + folder + '/' + block_type + '/combined_list/cmb_' + rule + '.txt'
                indir_path = '../results/exp/top' + str(topk) +\
                            '/' + folder + '/' + block_type + '/' + rule + '/'
                outpath = '../results/exp/top' + str(topk) +\
                            '/' + folder + '/' + block_type + '/combined_list/cmb_' + rule + '.txt'
                # field_corres = [('id', 'id'), ('name', 'name'), ('description', 'description'), ('price', 'price')]
                # field_corres = [('id', 'id'), ('name', 'name'), ('addr', 'addr'), ('city', 'city'),
                #                 ('phone', 'phone'), ('type', 'type'), ('class', 'class')]
                field_corres = [('id', 'id'), ('title', 'title'), ('description', 'description'),
                                ('manufacturer', 'manufacturer'), ('price', 'price')]
                # field_corres = [('id', 'id'), ('title', 'title'), ('category', 'category'),
                #                 ('brand', 'brand'), ('modelno', 'modelno'), ('price', 'price'),
                #                 ('proddescrlong', 'proddescrlong')]
                # field_corres = [('id', 'id'), ('title', 'title'), ('authors', 'authors'),
                #                   ('venue', 'venue'), ('year', 'year')]
                # field_corres = [('id', 'id'), ('title', 'title'), ('release', 'release'), ('artist_name', 'artist_name'),
                #                 ('duration', 'duration'), ('artist_familiarity', 'artist_familiarity'),
                #                 ('artist_hotttnesss', 'artist_hotttnesss'), ('year', 'year')]

                combine_recom_lists(indir_path, outpath, ltable_path, rtable_path, field_corres, 'id', 'id')
