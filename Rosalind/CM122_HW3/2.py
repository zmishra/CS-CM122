path = 'BBBABABBABABBBBABAAAABBBABBBAAAAABABBBABAABBBAABAA'
emissions = 'yyyxxyzzyzzxxyzyzzzzxxzyyyyxzyyzxyxxzxzxzyxyyxxzyy'

P = 1

for i in range(len(path)):
    if path[i] == 'A':
        if emissions[i] == 'x':
            P *= 0.112
        elif emissions[i] == 'y':
            P *= 0.613
        else:
            P *= 0.274
    else:
        if emissions[i] == 'x':
            P *= 0.204
        elif emissions[i] == 'y':
            P *= 0.58
        else:
            P *= 0.217

print(P)
