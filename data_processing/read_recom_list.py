import copy


def read_wrapped_recom_list(file, K):
    recom_lists = []
    infile = open(file, 'r')
    line = infile.readline()
    schema = line.split('@_@_@_@')
    for i in range(len(schema)):
        schema[i] = schema[i].rstrip('\n')
    lines = infile.readlines()
    start = 0
    while start < len(lines):
        recom_list = []
        K = int(lines[start])
        start += 1
        # print K
        for i in range(K):
            ltuple = []
            rtuple = []
            for j in range(len(schema)):
                ltuple.append(lines[start + 3 + j].rstrip('\n'))
                rtuple.append(lines[start + 3 + len(schema) + j].rstrip('\n'))
            recom_list.append((lines[start].strip(), lines[start + 1].strip(),
                               lines[start + 2].strip(), ltuple, rtuple))
            start += 3 + 2 * len(schema)
        recom_lists.append(copy.deepcopy(recom_list))
    return schema, recom_lists