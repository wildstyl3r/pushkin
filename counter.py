import string
f = open("p.txt", 'r', encoding='koi8-r')

source = f.read()

lines = source.split('\n')
letters = [c for c in source if c.isalpha()]
words = [word for word in [w.lower().strip(string.punctuation) for w in source.split()] if word != '']


print("Всего строк:", len(lines))
print("Всего букв:", len(letters))
print("Всего слов:", len(words))

words_len = [len(word) for word in words]
print("Средняя длина слова:", sum(words_len)/len(words_len))
print("Медианная длина слова:", sorted(words_len)[len(words_len)//2])

words_stats = {}
for word in words:
    if words_stats.get(word):
        words_stats[word] += 1
    else:
        words_stats[word] = 1

print("10 самых частых слов:", {key:value for key,value in sorted(words_stats.items(), key = lambda ws: ws[1], reverse=True)[:10]}) 
print(len([word for word in words if word[0]=='а']), "слов начинается на А или а")
