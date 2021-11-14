from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}
for character in sentence:
    if character in char_frequency:
        char_frequency[character] += 1
    else:
        char_frequency[character] = 1

pprint(char_frequency, width=1)

print(sorted(char_frequency.items()))
# print(list(char_frequency.items()))

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])
