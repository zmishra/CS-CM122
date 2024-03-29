def find_nth(str_, chr_, n):
    ind = str_.find(chr_)
    while ind >= 0 and n > 1:
        ind = str_.find(chr_, ind+1)
        n -= 1
    return ind


def occurrence(str_, n):
    chr_ = str_[n]
    cnt = 0
    ind = -1
    while ind != n:
        ind = str_.find(chr_, ind+1)
        cnt += 1
    return cnt


if __name__ == "__main__":
    last_col = "TTATAAAATGTCGGTCTGTCTAGTCCATAGTAAACCTGCCCTATCTGGTCATCCGTTATTACGTTAGAATCGCAATCGGTGGCACGGCCTACTGCATTATCGGGGGGCCTCGTACCGCTAAAACCAGCTTAACTCATCCGACGAGAGTGGAAATACCTGCCCCTCACACTTCCATCGCATCTTGGACATATACCCATTGTTTACTGGGCGATGCTTTATGGCCGAGGATCAATTAGTGTCGCGCGACTGTGATGTGGGCGCGACCCTGGCAACGTTCGGCACCTTGCGTTAGCCGAACGGCTCGCACTATGTCATCCTGAATGTTCCTGAGTAAGGGCTAACCGCGTACGACGTATGCTGCCACGCCACGCAAGACAGGTCGACGGCGGGTGCATGATAATGTTGTTGACCAATTTGTACGACCTATCCTGCTTCATTCA$TGAGGGTTAGCTGACGCCATCCCCCTAAACTTTGTCCTGGCCTGGTATAGAGACAGGCAAATTAACAATTGAACCTACCCCAAATCAAGGGCGACGTGTTACCTTGATTTAATTTGTTAGATTCGTCTCCATTGACCCTCGGGGGAGAAGAGCGTAGGTAGGAACGCACGAATAATGTGCGATCAAAAGGTGCCTACCTTCCTCTCGCTAAGAGTTATACCCGTATTACGAGGTTGCACTATTTTAGTAACGTGACAACCCGCATCATGTATGATCGGTCCGGAAAAAGTTAACCTCCTACTACTCAATTATCTGTGTCCGAATTTTGATATTAAGCTATAGTCACAGACTCGGCACACACTTTTCGCTATGGTCAGCCCCTGCGTTCATTTATTTGTAATGCTTTTCACTTAAGGCCGATTTCTAGACTTTCCAAAAGGTATAAAAATCAGGTTACTCTGCACTAAAGAGCTCACGTAAGAGTGTGCTCCATCTAAACTTGAGGATTTAG"
    first_col = "".join(sorted(last_col))
    output = ""
    ind = 0
    while len(output) != len(last_col)-1:
        c = last_col[ind]
        output = c + output
        ind = find_nth(first_col, c, occurrence(last_col, ind))
    print(output+"$")
