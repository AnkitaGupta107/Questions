import re


def dictionary_check(word_list,misspelt_word):
    output = []
    misspelt_word = misspelt_word.lower()
    misspelt_word_length = len(misspelt_word)

    #if misspelt_word in word_list:
    #    output.append(misspelt_word)

    for word in word_list:
        word_len = len(word)
        word_new = word.lower()
        sample_word = []
        for i in range(misspelt_word_length):
            if misspelt_word[i]==word_new[i]:
                sample_word.append(misspelt_word[i])
            new_word = ''.join(sample_word)
            if new_word in misspelt_word and (len(new_word) >2):
                output.append(word_new)
        print sample_word, new_word

    return set(output)



