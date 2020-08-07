# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
puns = set(['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'])

decoder_key = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def decode(filename):
    with open(filename) as f:
        text = f.read()
    # split each character
    letter_list = list(text)
    
    # character frequency analysis
    letter_count = {}
    for l in letter_list:
        if l not in letter_count:
            letter_count[l] = 0
        letter_count[l] += 1
    # print(letter_count)

    # sort by frequency
    sorted_letter_count = list(letter_count.items())
    sorted_letter_count.sort(key=lambda  kv: (-kv[1], kv[0]))
    # print(sorted_letter_count)

    # decode by frequency
    decoder = {}
    i = 0
    for char in sorted_letter_count:
        if char[0] in puns:
            decoder[char[0]] = decoder_key[i]
            i += 1
    # print(decoder)

    # decode 
    decoded_text = ""
    for l in letter_list:
        if l in decoder:
            decoded_text += f"{decoder[l]}"
        else:
            decoded_text += l
    # print(decoded_text)

    # save to file
    # output_file= open("ciphertext_decoded.txt", "w")
    # n = output_file.write(decoded_text)
    # output_file.close()


decode("ciphertext.txt")