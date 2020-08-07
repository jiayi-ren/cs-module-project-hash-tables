def word_count(s):
    # Your code here
    characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    for character in characters_to_ignore:
        s = s.replace(character, "")

    words = {}
    for word in s.lower().split():
        if word not in words:
            words[word] = 0
        words[word] += 1

    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))