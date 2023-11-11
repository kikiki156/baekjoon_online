word = input()
upword = word.upper()
lowword = word.lower()
for i in range(len(word)):
    if word[i] == upword[i]:
        print(lowword[i],end="")
    else:
        print(upword[i],end="")
    
"""
a = input()
print(a.swapcase())
"""

'''
print(input().swapcase())
'''