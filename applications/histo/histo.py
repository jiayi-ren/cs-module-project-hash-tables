# Your code here
def histo(filename):
    with open(filename) as f:
        text = f.read()

    char_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    for char in char_to_ignore:
        text = text.replace(char, "")
    
    words = {}
    for word in text.lower().split():
        if word not in words:
            words[word] = 0
        words[word] += 1
    
    # sorted_words = sorted(words.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    # for i in range(22):
    #     print( f"{list(sorted_words)[i][0]} {list(sorted_words)[i][1]}")

    sorted_words = list(words.items())
    sorted_words.sort(key=lambda e: (-e[1], e[0]))
    max_len = -1
    for word in sorted_words:
        if len(word[0]) > max_len:
            max_len = len(word[0])

    for i in range(len(sorted_words)):
        space = (max_len - len(sorted_words[i][0]) + 2)
        print( f"{sorted_words[i][0]}", " "* space, "#" *sorted_words[i][1])

histo("robin.txt")