import itertools

AA = 0.902
AB = 0.098
BA = 0.783
BB = 0.217

x = 'zxzyzzzxxyxzzzxyxyyzxyxyxxyzyzzyzzzxxzzzyzyxzyyyzyxxxzxxzyzzzxzyyyxxyyyyyzyzyxzyxxyyyxzzxzzzxxzzyyzy'
A_emissions = {'x':0.436, 'y':0.496, 'z':0.068}
B_emissions = {'x':0.568, 'y':0.319, 'z':0.113}

fwd_P = [[0 for c in x] for i in range(2)]

fwd_P[0][0] = 0.5*A_emissions[x[0]]
fwd_P[1][0] = 0.5*B_emissions[x[0]]

for i in range(1, len(x)):
    fwd_P[0][i] = (fwd_P[0][i-1]*AA + fwd_P[1][i-1]*BA) * A_emissions[x[i]]
    fwd_P[1][i] = (fwd_P[0][i-1]*AB + fwd_P[1][i-1]*BB) * B_emissions[x[i]]

P = fwd_P[0][len(x)-1] +fwd_P[1][len(x)-1]

print(fwd_P[0])
print(fwd_P[1])
print('')
print(P)