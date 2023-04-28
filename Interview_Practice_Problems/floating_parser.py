'''
Given a string like '-3.14' parse it into a valid float and throw an error for strings that are not numbers

doable in O(n) runtime complexity
 USE MODULUS!!!!

can iterate through string index by index

check it is a valid 'float'
    -can be done while iterating through string
need to handle negative sign
    -check if negative at start of string, if yes then start iterating through string at second index
need to handle period
    -
'''

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def parse_float(inputString):
    val = ''
    isNegative = inputString.startswith('-')
    isDecimal = False
    if isNegative:
        val = val + '-'
        for x in range(1, len(inputString)):
            if inputString[x] in alphabet:
                print('Not a valid float')
                return 0
            else:
                if inputString[x] == '-':
                    print('Not a valid float')
                    return 0
                elif inputString[x] == '.' and isDecimal == True:
                    print('Not a valid float')
                    return 0
                elif inputString[x] == '.' and isDecimal == False:
                    isDecimal = True
                    val = val + '.'
                else:
                    val = val + (str(int(inputString[x]) % 10))
    else:
        for x in inputString:
            if x in alphabet:
                print('Not a valid float')
                return 0

            else:
                if x == '-':
                    print('Not a valid float')
                    return 0
                elif x == '.' and isDecimal == True:
                    print('Not a valid float')
                    return 0
                elif x == '.' and isDecimal == False:
                    isDecimal = True
                    val = val + '.'
                else:
                    val = val + (str(int(x) % 10))

    print(float(val))


parse_float('-3.14')
parse_float('500.29')
parse_float('4a7g')
parse_float('--78.0')
parse_float('0.0.0')
