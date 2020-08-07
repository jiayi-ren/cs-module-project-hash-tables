def no_dups(s):
    # Your code here
    unique_word = {}
    res = ""
    for word in s.lower().split():
        if word not in unique_word:
            unique_word[word] = 1
            res += f"{word} "
    res = res.strip()
    return res


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))