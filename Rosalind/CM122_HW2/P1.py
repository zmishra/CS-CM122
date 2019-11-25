input_file = "manhat.txt"
content = [line.strip() for line in open(input_file).readlines()]
n = int(content[0].split(" ")[0])
m = int(content[0].split(" ")[1])

separation_index = content.index("-")

down = [[int(n) for n in content[i].split(" ")] for i in range(1, separation_index)]
right = [[int(n) for n in content[i].split(" ")] for i in range(separation_index+1, len(content))]

longest_path = [[0]*(m+1) for i in range(n+1)]

for i in range(1, n+1):
    longest_path[i][0] = longest_path[i-1][0] + down[i-1][0]
for j in range(1, m+1):
    longest_path[0][j] = longest_path[0][j-1] + right[0][j-1]
for i in range(1, n+1):
    for j in range(1, m+1):
        longest_path[i][j] = max(longest_path[i-1][j] + down[i-1][j], longest_path[i][j-1] + right[i][j-1])

print(longest_path[n][m])


