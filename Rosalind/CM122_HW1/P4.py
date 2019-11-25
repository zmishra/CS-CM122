f = open('rosalind_ini5.txt', 'r')
g = open('output.txt', 'w')
i = 1

for line in f:
    if i % 2 == 0:
        g.write(line)
    i = i + 1
