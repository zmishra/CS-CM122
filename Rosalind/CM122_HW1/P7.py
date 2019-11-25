chars = 'A B C D E F'
chars = chars.replace(' ', '')
n = 3
total_cnt = len(chars) ** n
words = ['']*total_cnt

for i in range(1, 6):
    char_cnt = int(total_cnt/(len(chars) ** i))
    for k in range(len(chars) ** i):
        for l in range(char_cnt):
            words[k*char_cnt + l] += chars[k % len(chars)]

for x in words:
    print(x)