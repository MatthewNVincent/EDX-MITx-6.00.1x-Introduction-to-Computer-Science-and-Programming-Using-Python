s = 'azcbobobegghakladekp'

solution = s[0]
start = 0
end = 0
i = 1

while i < len(s):
    if s[i-1] <= s[i]:
        end = i
    else:
        if end + 1 - start > len(solution):
            solution = s[start: end + 1]
        start = i
        end = i
    i += 1

if end + 1 - start > len(solution):
    solution = s[start: end + 1]

print('Longest substring in alphabetical order is: ' + solution)
