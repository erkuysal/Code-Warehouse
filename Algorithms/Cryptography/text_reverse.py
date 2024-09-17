

message = 'Reverse Text'
message_reversed = ''

print('Length of the message: ', len(message))

i = len(message) - 1

while i >= 0:
    message_reversed = message_reversed + message[i]
    print(f'Current reversed message is: {message_reversed}')
    i = i - 1

print(f'Reversed Message : {message_reversed}')




