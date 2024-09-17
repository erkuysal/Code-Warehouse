LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

message = 'GaPjEyTnAuRlVpKeQkPjVp'

for key in range(len(LETTERS)):
    translated = ''

    for letter in message:
        if letter in LETTERS:
            num = LETTERS.find(letter)
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:
            translated = translated + letter

        # print(translated)

    print('Hacking Key #%s: %s' % (key, translated))