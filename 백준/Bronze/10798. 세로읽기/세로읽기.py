rows = 5
max_len = 15
words = []
for i in range(5) :
    word = input()
    words.append(word)



for j in range(max_len) :
    for i in range(rows) :
        if j < len(words[i]) :
            print(words[i][j], end='')