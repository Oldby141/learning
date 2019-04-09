S = input().strip()
list_s = []
for i in range(len(S)):
    list_s.append(S[i])
list = []
list.append(S)
for i in range(len(S)):
    first = list_s[0]
    list_s.remove(first)
    list_s.append(first)
    s = "".join(list_s)
    if s not in list:
        list.append(s)
print(len(list))