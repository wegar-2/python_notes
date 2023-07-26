from string import ascii_lowercase

str1 = ascii_lowercase[:10]
str2 = ascii_lowercase[10:]

l1 = list(str1)
l2 = list(str2)

l3 = l1.copy()
print(l3)
l3.append(l2)
print(l3)


l1.extend(l2)
print(l1)

