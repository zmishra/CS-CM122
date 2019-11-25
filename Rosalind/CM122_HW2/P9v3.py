def pairwise_alignment(ref, donor):
    output_matrix = [[0] * (len(donor) + 1) for i in range(len(ref) + 1)]
    trace_matrix = [[0] * (len(donor) + 1) for i in range(len(ref) + 1)]

    for i in range(len(ref) + 1):
        output_matrix[i][0] = -i
        trace_matrix[i][0] = 1
    for j in range(len(donor) + 1):
        output_matrix[0][j] = -j
        trace_matrix[0][j] = 0

    for j in range(1, len(donor) + 1):
        for i in range(1, len(ref) + 1):
            deletion = output_matrix[i - 1][j] - 1
            insertion = output_matrix[i][j - 1] - 1
            identity = output_matrix[i - 1][j - 1] if ref[i-1] == donor[j-1] else -9999999999
            substitution = output_matrix[i - 1][j - 1] - 1 if ref[i-1] != donor[j-1] else -9999999999
            val, idx = max((val, idx) for (idx, val) in enumerate([insertion, deletion, identity, substitution]))
            output_matrix[i][j] = val
            trace_matrix[i][j] = idx

    i = len(ref)
    j = len(donor)
    refnew = ''
    donornew = ''
    while i != 0 or j != 0:
        if trace_matrix[i][j] == 2 or trace_matrix[i][j] == 3:
            refnew = ref[i - 1] + refnew
            donornew = donor[j - 1] + donornew
            i -= 1
            j -= 1
        elif trace_matrix[i][j] == 1:
            donornew = '-' + donornew
            refnew = ref[i - 1] + refnew
            i -= 1
        else:
            donornew = donor[j - 1] + donornew
            refnew = '-' + refnew
            j -= 1
    return refnew, donornew, val


def count_mismatches(list_):
    score = 0
    for i in range(len(list_)):
        for j in range(i + 1, len(list_)):
            if list_[i] != list_[j]:
                score += 1
    return score


if __name__ == '__main__':
    #seq = ['ATATCCG', 'TCCG', 'ATGTACTG', 'ATGTCTG']
    seq = ['GACGCTACAT', 'CTAGGACG', 'GACACCCCG', 'CATGATCCTC']
    _01_23 = [pairwise_alignment(seq[0], seq[1]), pairwise_alignment(seq[2], seq[3])]
    print(_01_23)
    _02_13 = [pairwise_alignment(seq[0], seq[2]), pairwise_alignment(seq[1], seq[3])]
    print(_02_13)
    _03_12 = [pairwise_alignment(seq[0], seq[3]), pairwise_alignment(seq[1], seq[2])]
    print(_03_12)

    if _01_23[0][2]+_01_23[1][2] >= _02_13[0][2]+_02_13[1][2] and _01_23[0][2]+_01_23[1][2] >= _03_12[0][2]+_03_12[1][2]:
        pair1 = [_01_23[0][0], _01_23[0][1]]
        pair2 = [_01_23[1][0], _01_23[1][1]]
    elif _02_13[0][2]+_02_13[1][2] >= _03_12[0][2]+_03_12[1][2]:
        pair1 = [_02_13[0][0], _02_13[0][1]]
        pair2 = [_02_13[1][0], _02_13[1][1]]
    else:
        pair1 = [_03_12[0][0], _03_12[0][1]]
        pair2 = [_03_12[1][0], _03_12[1][1]]

    pair1 = [_02_13[0][0], _02_13[0][1]]
    pair2 = [_02_13[1][0], _02_13[1][1]]
    print(pair1, pair2)

    output = [[0] * (len(pair2[0]) + 1) for i in range(len(pair1[0]) + 1)]
    trace = [[0] * (len(pair2[0]) + 1) for i in range(len(pair1[0]) + 1)]

    for i in range(1, len(pair1[0]) + 1):
        output[i][0] = output[i-1][0] - count_mismatches([pair1[0][i-1], pair1[1][i-1], '-', '-'])
        trace[i][0] = 1
    for j in range(1, len(pair2[0]) + 1):
        output[0][j] = output[0][j-1] - count_mismatches([pair2[0][j-1], pair2[1][j-1], '-', '-'])
        trace[0][j] = 0

    for j in range(1, len(pair2[0]) + 1):
        for i in range(1, len(pair1[0]) + 1):
            deletion = output[i - 1][j] - count_mismatches([pair1[0][i-1], pair1[1][i-1], '-', '-'])
            insertion = output[i][j - 1] - count_mismatches([pair2[0][j-1], pair2[1][j-1], '-', '-'])
            idorsub = output[i - 1][j - 1] -  count_mismatches([pair1[0][i-1], pair1[1][i-1], pair2[0][j-1], pair2[1][j-1]])
            val, idx = max((val, idx) for (idx, val) in enumerate([insertion, deletion, idorsub]))
            output[i][j] = val
            trace[i][j] = idx

    i = len(pair1[0])
    j = len(pair2[0])
    pair1_new = ['', '']
    pair2_new = ['', '']
    while i != 0 or j != 0:
        if trace[i][j] == 2:
            pair1_new[0] = pair1[0][i - 1] + pair1_new[0]
            pair1_new[1] = pair1[1][i - 1] + pair1_new[1]
            pair2_new[0] = pair2[0][j - 1] + pair2_new[0]
            pair2_new[1] = pair2[1][j - 1] + pair2_new[1]
            i -= 1
            j -= 1
        elif trace[i][j] == 1:
            pair2_new[0] = '-' + pair2_new[0]
            pair2_new[1] = '-' + pair2_new[1]
            pair1_new[0] = pair1[0][i - 1] + pair1_new[0]
            pair1_new[1] = pair1[1][i - 1] + pair1_new[1]
            i -= 1
        else:
            pair2_new[0] = pair2[0][j - 1] + pair2_new[0]
            pair2_new[1] = pair2[1][j - 1] + pair2_new[1]
            pair1_new[0] = '-' + pair1_new[0]
            pair1_new[1] = '-' + pair1_new[1]
            j -= 1

    final_alignment = [pair1_new[0], pair1_new[1], pair2_new[0], pair2_new[1]]

    score = 0
    for i in range(len(pair1_new[0])):
        for j in range(len(final_alignment)):
            for k in range(j + 1, len(final_alignment)):
                if final_alignment[j][i] != final_alignment[k][i]:
                    score -= 1

    print(score)
    print(pair1_new[0])
    print(pair1_new[1])
    print(pair2_new[0])
    print(pair2_new[1])

