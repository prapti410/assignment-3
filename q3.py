def reversed_words(sentence):
    list_of_words= sentence.split()
    list_of_words.reverse()
    reversed_line = " ".join(list_of_words)
    print(reversed_line)

    reversed_words("I am coming")
    reversed_words("we are coming")
