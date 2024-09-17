
def split_len(sequence, length):
    return [sequence[i:i + length] for i in range(0, len(sequence), length)]


def encode(key, raw_text):

    order = {
        int(value): num for num, value in enumerate(key)
    }

    ciphertext = ''

    for index in sorted(order.keys()):
        for part in split_len(raw_text, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue

    return ciphertext


print(encode('3210', "Hello"))
