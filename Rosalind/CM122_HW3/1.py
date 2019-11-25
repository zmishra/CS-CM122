path = 'BBBABBABABBBBBBBBBAAAAAABAABBBAABAABAABBAABAABBABA'

P = 0.5
first = False
prev = 'B'

for c in path:
    if first:
        if prev == 'A':
            if c == 'A':
                prev = 'A'
                P *= 0.448
            else:
                prev = 'B'
                P *= 0.552
        else:
            if c == 'A':
                prev = 'A'
                P *= 0.845
            else:
                prev = 'B'
                P *= 0.155
    else:
        first = True

print(P)
