def shuffle(s, t):
    """'"""
    if s == "":
        return [t]
    if t == "":
        return [s]
    else: #s,t != ""
        i = 0
        list1 = shuffle(s[1:],t)
        while i < len(list1):
            list1[i] = s[0] + list1[i]
            i += 1
        i = 0
        list2 = shuffle(s,t[1:])
        while i < len(list2):
            list2[i] = t[0] + list2[i]
            i += 1
        list3 = list1 + list2 
        list3 = set(list3)
        list3 = list(list3)
        return list3


print(sorted(shuffle('ab', 'cd')))