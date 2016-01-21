s = 'azcbobobegghaklbob'

result = 0

for i in range(len(s)-2):
    if s[i: i+3] == 'bob':
        result += 1

print('Number of times bob occurs is: ' + str(result))
