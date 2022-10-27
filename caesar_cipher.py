alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Do o want to encode or decode the message: ').lower()


if direction == 'encode':
    msg_to_encode = input('Type your message to encode: ').lower()
    shift = int(input('How many shifts?: '))
    enMessage = ' '
    for i in msg_to_encode:
        if i in alphabet:
            position = alphabet.index(i)
            enMessage+= alphabet[(position + shift)%26]
    print(enMessage)

if direction == 'decode':
    msg_to_decode = input('Type your message to encode: ').lower()
    shift = int(input('How many shifts?: '))
    deMsg = ''
    for i in msg_to_decode:
        if i in alphabet:
            position = alphabet.index(i)
            deMsg += alphabet[(position - shift)%26]
    print(deMsg)
else:
    print('Wrong input: type encode or decode')
# yexodxs