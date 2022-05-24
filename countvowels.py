def countvowel(x):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in x:
        if letter.lower() in vowel:
            count += 1
    return count