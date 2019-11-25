def count_mismatches(list_):
    score = 0
    for i in range(len(list_)):
        for j in range(i + 1, len(list_)):
            if list_[i] != list_[j]:
                score += 1
    return score


if __name__ == '__main__':
    seq1 = 'AA'
    seq2 = 'AA'
    seq3 = 'AA'
    seq4 = 'BBBBBBBBB'

    output_matrix = [[[[0]*(len(seq4)+1) for i in range(len(seq3)+1)] for j in range(len(seq2)+1)] for k in range(len(seq1)+1)]
    for i in range(len(seq1)+1):
        output_matrix[i][0][0][0] = -i*3

    for j in range(len(seq2)+1):
        output_matrix[0][j][0][0] = -j*3

    for k in range(len(seq3)+1):
        output_matrix[0][0][k][0] = -k*3

    for l in range(len(seq4) + 1):
        output_matrix[0][0][0][l] = -l*3

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            output_matrix[i][j][0][0] = output_matrix[i-1][j-1][0][0] - count_mismatches([seq1[i-1], seq2[j-1], '-', '-'])



    for l in range(1, len(seq4) + 1):
        for k in range(1, len(seq3) + 1):
            for j in range(1, len(seq2) + 1):
                for i in range(1, len(seq1) + 1):
                    A_ = output_matrix[i-1][j-1][k-1][l-1] - count_mismatches([seq1[i-1], seq2[j-1], seq3[k-1], seq4[l-1]])
                    B_ = output_matrix[i][j-1][k-1][l-1] - count_mismatches(['-', seq2[j-1], seq3[k-1], seq4[l-1]])
                    C_ = output_matrix[i-1][j][k-1][l-1] - count_mismatches([seq1[i-1], '-', seq3[k-1], seq4[l-1]])
                    D_ = output_matrix[i-1][j-1][k][l-1] - count_mismatches([seq1[i-1], seq2[j-1], '-', seq4[l-1]])
                    E_ = output_matrix[i-1][j-1][k-1][l] - count_mismatches([seq1[i-1], seq2[j-1], seq3[k-1], '-'])
                    F_ = output_matrix[i][j][k-1][l-1] - count_mismatches(['-', '-', seq3[k-1], seq4[l-1]])
                    G_ = output_matrix[i][j-1][k][l-1] - count_mismatches(['-', seq2[j-1], '-', seq4[l-1]])
                    H_ = output_matrix[i][j-1][k-1][l] - count_mismatches(['-', seq2[j-1], seq3[k-1], '-'])
                    I_ = output_matrix[i-1][j][k][l-1] - count_mismatches([seq1[i-1], '-', '-', seq4[l-1]])
                    J_ = output_matrix[i-1][j][k-1][l] - count_mismatches([seq1[i-1], '-', seq3[k-1], '-'])
                    K_ = output_matrix[i-1][j-1][k][l] - count_mismatches([seq1[i-1], seq2[j-1], '-', '-'])
                    L_ = output_matrix[i][j][k][l-1] - count_mismatches(['-', '-', '-', seq4[l-1]])
                    M_ = output_matrix[i][j][k-1][l] - count_mismatches(['-', '-', seq3[k-1], '-'])
                    N_ = output_matrix[i][j-1][k][l] - count_mismatches(['-', seq2[j-1], '-', '-'])
                    O_ = output_matrix[i-1][j][k][l] - count_mismatches([seq1[i-1], '-', '-', '-'])

                    val, idx = max((val, idx) for (idx, val) in enumerate([A_, B_, C_, D_, E_, F_, G_, H_, I_, J_, K_, L_, M_, N_, O_]))
                    output_matrix[i][j][k][l] = val

    print(output_matrix[len(seq1)][len(seq2)][len(seq3)][len(seq4)])

