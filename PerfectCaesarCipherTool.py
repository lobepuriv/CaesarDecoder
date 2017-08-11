alphabet = ['A','B','C','D','E','F','G','H','I',
            'J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z']

# by FarinHeiT a.k.a. valsoraY vk.com/farinheit Python 1Love :D 06.03.17 23:25 off release :D

# encoding with '+3' letters shift
def Encode(text):
    list1 = list(text)
    for i in range(len(list1)):
        for j in range(26):
            if list1[i] == alphabet[j]:
                if j + 3 > 25:
                    list1[i] = alphabet[j+3 - 26]
                    break
                list1[i] = alphabet[j + 3]
                break
    return ''.join(list1)

# decoding with '-3' letters shift
def Decode(text):
    list1 = list(text)
    for i in range(len(list1)):
        for j in range(26):
            if list1[i] == alphabet[j]:
                if j - 3 < 0:
                    list1[i] = alphabet[26 - abs(j - 3)]
                    break
                else:
                    list1[i] = alphabet[j - 3]
                    break
    return ''.join(list1)

# try all possible variants
def Brute(text):
    list1 = list(text)
    ii = 0
    print('\n'+'*'*35)
    while ii < 26:
        for i in range(len(list1)):
            for j in range(26):
                if list1[i] == alphabet[j]:
                    if j - ii < 0:
                        list1[i] = alphabet[26 - abs(j - ii)]
                        break
                    else:
                        list1[i] = alphabet[j - ii]
                        break
        print('Shift '+str(ii),''.join(list1))
        list1 = list(text)
        ii += 1
    print('\n'+'*'*35)
    return 'Look upon dude :)'

while True:
    choice = input('\nby FarinHeiT 06.03.17\nWhat you wanna do?\n d - decode\n e - encode\n b - brute\n')
    if choice == 'd' or choice == 'decode':
        text = input('Enter text to decode: ').upper()
        print('\n'+'*'*35+'\nDecoded text: ',Decode(text),'\n'+'*'*35)
    elif choice == 'e' or choice == 'encode':
        text = input('Enter text to encode: ').upper()
        print('\n'+'*'*35+'\nEncoded text: ',Encode(text),'\n'+'*'*35)
    elif choice == 'b' or choice == 'brute':
        text = input('Enter text to brute: ').upper()
        print(Brute(text))
    else:
        print('\nInvadid choice dude :(')

