def high_entropy_passphrases(passphrases):
    valid_phrases = 0
    for phrase in passphrases:
        phrase = phrase.strip().split(' ')
        phrase.sort()
        i = 0
        valid = True
        while i < (len(phrase) - 1) and valid:
            if phrase[i] == phrase[i + 1]:
                valid = False
            i += 1

        if valid:
            valid_phrases += 1
    print valid_phrases

f = open('04_input.txt', 'r')
passphrases = f.readlines()

high_entropy_passphrases(passphrases)
