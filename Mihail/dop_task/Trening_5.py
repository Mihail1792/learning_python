from collections import Counter
import re

words = ""
lines = 0

with open('/Users/mihail/Documents/11.txt', 'r') as my_text:
    s = my_text.read()
    for i in s:
        paragraph = len(s.split('\n\n'))
        if i.isalpha():
            words += i
    f = re.split(r"[.!?]+", s)
    for k in f:
        lines += 1

print(f'Десять самые часто встречаемых букв: {Counter(words).most_common(10)}\n'
      f'Количество предложений: {lines}\nКоличество абзацев: {paragraph}')














# f = re.split(r'[.!?]+', s)
# print(f)

# lines += re.split(r'[.!?]+', s)





# есть файл referat.txt

# **** Задание, открыть питоном файл, прочитать его, вывести на экран:
# **** Количество абзацев в реферате: N
# **** Количество предложений в реферате: N
# **** 10 самых часто встречаемых символов: список в порядке убывания
# **** 10 самых часто встречаемых символов.

# ******
# сплит по точке
# requests библиотека выучить (GET, POST запросы, query параметры head body запроса, response,
# json, HTTP протокол как работает)
# ******
import collections
from collections import Counter





# print(words)
# print(my_text.read())




# lines = 0
# paragraph = 1
# letters = 0
# sentence = 1
# words = 0
# with open('11.txt', 'r') as my_text:
#     for s in my_text:
#         words = s.split('.')
# print(Counter(words))

# c = collections.Counter()

# c = Counter('abcacdabcacd')
# print(c)
#
# s = 'the lazy dog jumped over another lazy dog'
# words = s.split()
# print(Counter(words))



# d = 0
# with open('11.txt', 'r') as my_text:
#     for sentence in my_text:
#         c[sentence] += 1
#     for words in my_text:
#         d += words.split()
# print(d)
#
#
# print(c.most_common(2))
#
# print(c)


    # for c in my_text:
    #     Counter(my_text).most_common(10)
    #     d[c] += 1
    # print(d)




#
#     for word in my_text:
#         c[word] += 1
#         print(c['counter'])


# import os
#
# paragraph = 1
#
# with open('11.txt', 'r') as my_text:
#     s = my_text.read()
#     for i in s:
#         if i == os.linesep:
#             paragraph += 1
#
# print(f'Количество абзацев: {paragraph}')

#
# with open('11.txt', 'r') as my_text:
#     s = my_text.read()
#     for i in s:
#         x = s.split('\n\n')
#
# # x = "Blabla".split('\n\n')
# print(len(x))








# check_string = "fffgsfhg, akklej"






# count = {}
# for s in check_string:
#   if count.has_key(s):
#     count[s] += 1
#   else:
#     count[s] = 1
#
# for key in count:
#   if count[key] > 1:
#     print key, count[key]












# with open('11.txt', 'r') as my_text:
#     bukvy = 0
#     predlojenija = 0
#
#     for k in my_text:
#         if k != ' ' and k != '.' and k != '?' and k != ',' and k != '"':
#             bukvy += len(k)
#         predlojenija += k.count('.') + k.count('!') + k.count('?')
#
#     print(f'Буквы: {bukvy}, Предложения:{predlojenija}')













# tekst = "fs, yt oi. Ag. Td! ii?"
#
# lines = 0
# words = 0
# letters = 0
#
# for line in tekst:
#     lines += 1
#     letters += len(line)
#
#     pos = 'out'
#     for letter in line:
#         if letter != ' ' and pos == 'out':
#             words += 1
#             pos = 'in'
#         elif letter == ' ':
#             pos = 'out'
#
# print("Lines:", lines)
# print("Words:", words)
# print("Letters:", letters)










# s = 'the lazy dog jumped over another lazy dog'
#
# d = Counter(s).most_common(3)
# print(d)



# a = Counter('superfluous')

# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})
# print(a)
#
# counter = Counter('superfluofgfgfggilu;gyftdfjghgklhgyukjus')
# print(counter).most_common(3)  # 3
#
# d = string.ascii_uppercase
# print(d)


