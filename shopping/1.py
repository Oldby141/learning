while True:
    try:
        S = input().strip()
        list_s = []
        for i in range(len(S)):
            list_s.append(S[i])
        count = 1
        list = []
        list.append(list_s)
        for i in range(len(S)):
            first = list_s[0]
            list_s.remove(first)
            list_s.append(first)
            s = "".join(list_s)
            for x in list:
                if x!=s:
                    list.append(s)
        print(len(list))

    except:
        break