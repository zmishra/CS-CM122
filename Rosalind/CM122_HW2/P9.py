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
    return refnew, donornew


if __name__ == '__main__':
    seq = ['GACGCTACAT', 'CTAGGACG', 'GACACCCCG', 'CATGATCCTC']

    guide = seq[3]
    pa1 = pairwise_alignment(guide, seq[0])
    pa2 = pairwise_alignment(guide, seq[1])
    pa3 = pairwise_alignment(guide, seq[2])

    #merge pa1 and pa2
    i = 0
    j = 0
    seq1a = ''
    seq2a = ''
    seqga = ''
    while i < len(pa1[0]) and j < len(pa2[0]):
        if pa1[0][i] == pa2[0][j]:
            seqga += pa1[0][i]
            seq1a += pa1[1][i]
            seq2a += pa2[1][j]
            i += 1
            j += 1
        else:
            if pa1[0][i] == '-':
                seqga += pa1[0][i]
                seq1a += pa1[1][i]
                seq2a += '-'
                i += 1
            else:
                seqga += pa2[0][j]
                seq1a += '-'
                seq2a += pa2[1][j]
                j += 1

    #merge pa3
    i = 0
    j = 0
    seq1b = ''
    seq2b = ''
    seq3b = ''
    seqgb = ''
    while i < len(seqga) and j < len(pa3[0]):
        if seqga[i] == pa3[0][j]:
            seqgb += pa3[0][j]
            seq1b += seq1a[i]
            seq2b += seq2a[i]
            seq3b += pa3[1][j]
            i += 1
            j += 1
        else:
            if seqga[i] == '-':
                seqgb += seqga[i]
                seq1b += seq1a[i]
                seq2b += seq2a[i]
                seq3b += '-'
                i += 1
            else:
                seqgb += pa3[0][j]
                seq1b += '-'
                seq2b += '-'
                seq3b += pa3[1][j]
                j += 1

    final_alignment = [seqgb, seq1b, seq2b, seq3b]

    score = 0
    for i in range(len(seqgb)):
        for j in range(len(final_alignment)):
            for k in range(j+1, len(final_alignment)):
                if final_alignment[j][i] != final_alignment[k][i]:
                    score -= 1

    print(score)
    print(seqgb)
    print(seq1b)
    print(seq2b)
    print(seq3b)







