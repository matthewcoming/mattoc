sentence = input('Enter a sentence\n')
print('\nThis is your sentence backwards:')
words = sentence.split()
words.reverse()
print(' '.join(words))