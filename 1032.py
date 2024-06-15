a = int(input())
if a == 1:
    print(input())
else:
    right_word = list(input())
    for i in range(1,a):
        input_word = list(input())
        for j in range(len(right_word)):
            if right_word[j] == "?":
                pass
            else:
                if input_word[j] != right_word[j]:
                    right_word[j] = "?"
    print(''.join(right_word))