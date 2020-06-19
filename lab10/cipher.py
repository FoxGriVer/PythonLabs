def decipher(msg, perm):
    all_words_in_msg = list(msg)
    code_dict = dict()
    eng_alph = list("abcdefghijklmnopqrstuvwxyz")
    cripted_perm = list(perm)

    counting_position = 0
    code_dict[" "] = " "
    for letter in eng_alph:
        code_dict[letter] = cripted_perm[counting_position]
        counting_position += 1

    decoded_string = ""
    for word in all_words_in_msg:
        letters_in_word = list(word)
        for letter in letters_in_word:
            decoded_string += list(code_dict.keys())[
                list(code_dict.values()).index(letter)
                ]

    return decoded_string


perm = "wnoegbjpkyxlfiuastqhvmcrzd"
decipher("hpg ntuci bur yvfaq umgt hpg euj", perm)
