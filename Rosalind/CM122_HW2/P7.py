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
    input = "GTAACAACCTAGCTCGTTTAATATATATTAAATAAATATTGTGGACCCTGAGGGCTACTGAACCAAATGCGTACACTTCAGGTATATAATGCCACTGTAGCGGGATACTTTCGGGCTGGCGAGTTGTTGATCTGGGGCACATGCTGTTATAATACGTCTATTTTCTGTAGGCGCCCACAGGTGGTAACTAGAGGAAGTAGAAAACTACGTAGAGGAATCCTTGGGTGCTATTCTAATATCTTGGCACGGGGGCTGGGAGCGCGCTTGGCCTTTAACACTAGACGAGTTTGATGGGTATGAGTGTTTGTTTGCTCACCGAATCGGATTTAAACTCGGGCATATTATGGAGGGAATAGGATCTTATAAAATGACGCTCTGCCCCACGAAATATCGCGGCGCTGTTTAGCGGATCGCTCTTTCGTACTACGTCTTTGTCAATAAACTAGCTAAGCGAGCACAACTATCTCTTACCCTTGGGCAGACACGACCGTGTGATAAGGACCGCGAACTGGAGGATACTCCCAGATCCATGTTGGCCCTATCCAGTATCAAACTACCGCGCTCGGTGCACCCTTGGTCGCAGGCACGTCCGCTATGCCGATTATTTGCTGATGAGTGATAGTTCTCTCATTCTAAATCTAAGTAGGAGCGCGCTGAGGAATTCACAGTGGTTGCAACGCGTTTTAGCTGAGGCACGAATGAGACATCCCCCGCGCGGGGCTAACATTCGCGGGACCCCAACGAGGTAAGAGTTAAACCTCTTCTGCTGTCCATTGTCAGGTTCCGTCACCAGCAAAACCGCCTCTGCCTGTCGAGTGCAGGGGCCTCTGTCCCGACTAAGGTAGCAAAGTGTGTTTGCCGTTGACAGACAGGTCACTCGCAGTGGTAAGCTCGTTTGACATTGTAGCCTGCGCCCTTAAATCGCCACCGCGAAATCCTATTAGCTTGAGCGCGCCCACC$"
    n = 423

    sorted_input = "".join(sorted(input))

    print(find_nth(sorted_input, input[n], occurrence(input, n)))
