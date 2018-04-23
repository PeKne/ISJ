#!/usr/bin/env python3
import fileinput

reversed_list = set([])
result = []

for line in fileinput.input():
    word = line.rstrip()
    reversed_word = word[::-1]
    if not word == reversed_word: #its not palindrom
        reversed_list.add(reversed_word)
        if word in reversed_list: #if got match
            result.append(word)
            result.append(reversed_word)

print(sorted(result))
