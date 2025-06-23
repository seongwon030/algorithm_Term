from collections import defaultdict
import random

with open('HarryPotter.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

clean_text = ' '.join(raw_text.split())
arr = clean_text.split(' ')

markov = defaultdict(list)

for i in range(len(arr)-2):
    prefix = arr[i] + ' ' + arr[i+1]
    suffix = arr[i+2]
    markov[prefix].append(suffix)

max_words = 98
s = input()
print(s, end = ' ')

while True:
    keys = markov[s]
    key_list = list(set(keys))
    if len(key_list) > 1:
        next_word = key_list[random.randint(0,len(key_list)-1)]
    else:
        next_word = key_list[0]

    if next_word == '[end]':
        break
    print(next_word, end = ' ')
    max_words -= 1
    if max_words == 0:
        break
    s = s.split(' ')[1] + ' ' + next_word