import re
from collections import defaultdict

search = "XMAS"

word_search = []
while True:
    try:
        word_search.append(input())
    except EOFError:
        break

total_found = 0

for i in range(1, len(word_search[0])-1):
    for j in range(1, len(word_search)-1):
        if word_search[j][i] == 'A':
            letter_count = defaultdict(int)
            letter_count[word_search[j-1][i-1]] += 1
            letter_count[word_search[j-1][i+1]] += 1
            letter_count[word_search[j+1][i-1]] += 1
            letter_count[word_search[j+1][i+1]] += 1
            if word_search[j+1][i-1] != word_search[j-1][i+1] and letter_count['M'] == 2 and letter_count['S'] == 2:
                total_found += 1

print(total_found)