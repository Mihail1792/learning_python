a = (1, 4, 3, 7, 1, 6, 1)
my_list = []
counter = 0
for i in a:
    if i == 1:
        counter += 1
my_list.append(counter)
print(my_list)

d = 3 in my_list
print(d)



# b = 3 in a
# print(b)
# с помощью этого выражения можно без цикла проверить вхождения чего-либо в итерируемый объект