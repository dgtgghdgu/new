# -*- conding:Utf-8 -*-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words."""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off.
    :type words: object
    """
    word = words[0]
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words[-1]
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("This is time to show:")
print("I can play. tran a sentence to sort word")
print("Let's do it")

inputword = input("Please type a word or sentence:")

print("这是分隔的文字")
print(break_words(inputword))
print("---------------------")
print("这是分隔加排序的")
print(sort_words(break_words(inputword)))
print("---------------------")
print("打印第一个字母")
print_first_word(inputword)
print("---------------------")
print("打印最后一个字母")
print_last_word(inputword)
print("---------------------")
print("打印第一个和最后一个单词")
print_first_and_last(inputword)
print("---------------------")
print("打印排序后第一个和最后一个单词")
print_first_and_last_sorted(inputword)