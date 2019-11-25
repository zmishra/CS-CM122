import numpy as np

transition_string = """
0.303	0.661	0.037; 
0.317	0.203	0.481; 
0.455	0.405	0.14
"""

emission_string = """
0.54	0.16	0.3; 
0.337	0.354	0.308; 
0.308	0.324	0.369
"""

A = np.array(np.matrix(transition_string))
# print(A)
B = np.array(np.matrix(emission_string))
# print(B)

x = 'xxxyzyxyyxyzyyxyyxyyyzzyzyzxzzyzxxyzyyxxzzyyyzxyzxyzzzyzyzzyxzxzxyzxzyyzzxxxxxzxzyzxyzzzxzyxzzzyyzyz'
y = [0 if c == 'x' else 1 if c == 'y' else 2 for c in x]

K = A.shape[0]
Pi = np.ones(K)/K

T1 = np.zeros((K, len(x)))
T2 = np.zeros((K, len(x)))

T1[:, 0] = Pi * B[:, y[0]]

for j in range(1, len(x)):
    for i in range(K):
        T1[i, j] = np.max(T1[:, j-1]*A[:, i]*B[i, y[j]])
        T2[i, j] = np.argmax(T1[:, j-1]*A[:, i])

result = ''
z = [0]*len(x)

z[len(x)-1] = np.argmax(T1[:, len(x)-1])
result = chr(z[len(x)-1] + 65) + result

for k in reversed(range(1, len(x))):
    z[k-1] = int(T2[z[k], k])
    result = chr(z[k-1] + 65) + result

print(result)

