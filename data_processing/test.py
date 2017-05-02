from os import listdir
from os.path import isfile
import pandas as pd

def read_files(dir):
    d = {}
    files = listdir(dir)
    for file in files:
        K = int(file.split('_')[0].replace('top', ''))
        fin = open(dir + file)
        lines = fin.readlines()
        d[K] = float(lines[1])

    s = ''
    for i in range(15):
        s += str(d[(i + 1) * 100]) + ','
    print s


def test_dtype():
    s = pd.Series([1, 2, 3, 414123])
    print s.dtype

if __name__ == "__main__":
    # dir = '../../Song-Song/new_topk_para_reuse/'
    # read_files(dir)

    test_dtype()