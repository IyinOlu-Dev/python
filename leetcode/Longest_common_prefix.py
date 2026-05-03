strs = ["flower","flow","flight"]
# strs = ["dog","cat","bat"]

a = list (strs[0])

for word_index in range (1, len(strs)):
    prefix = []
    for i, char_index in enumerate(strs[word_index]):
        if i >= len(a):
            break
        if a[i] == char_index:
            prefix.append(a[i])
        else:
            break
    a = prefix.copy()
if len(prefix) == 0:
    print("")
else:   
    print("".join(prefix))



