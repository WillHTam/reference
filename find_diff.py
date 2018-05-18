import difflib
text1 = open('./1.txt', 'rb').read()
text2 = open('./2.txt', 'rb').read()

s = difflib.SequenceMatcher(None, text1, text2)
m = s.get_matching_blocks()

for oc in s.get_opcodes():
    print("%8s %s <=> %s" % (oc[0], repr(text1[oc[1]:oc[2]]), repr(text2[oc[3]:oc[4]])))

