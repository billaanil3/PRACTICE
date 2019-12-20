def subStrings(s):
    import pdb
    pdb.set_trace()
    for i in range(len(s)):
        for res in range(i + 1, len(s) + 1):
            print s[i:res]

s = 'anil'
subStrings(s)
