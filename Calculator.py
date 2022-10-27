
def syntaxOkay(string):
    """check if the string is an allowed mathematical expression
    :param string: the string to check
    :return: True or False"""
    nums = list(map(str, range(0,10)))
    operators = ['+', '-', '*', '/',]
    allowed = operators + ['A', 'Z'] + nums
    bracket = [] # originally it's a stack, but it works just as well
    last = None
    for char in string:
        if char == ' ':
            continue
        if not char in allowed: #could use a hashmap to make it quicker runtime
            #print(char,'is not an allowed string')
            msg = char+' is not an allowed string'
            return False, msg
        if char == 'A':
            bracket.append(char)
        if char == 'Z':
            try:    # could be empty
                bracket.pop()
            except IndexError:
            # if the list is empty and there's a 'Z' it's wrong
                #print('closed brackets without opening them')
                return False, 'closed brackets without opening them'
        if last is None:
            # it's the first one
            if char == '*' or char == '/' or char == 'Z':
                #print("can't start with",char,"charcter")
                return False, "can't start with "+char+" charcter"
        if last in operators:
            if char in ['+', '*', '/', 'Z']:
                #print("can't put '"+char+"' after an operator")
                return False, "can't put '"+char+"' after an operator"
        last = char
    if bracket == []:
        return True, ''
    else:
        #print('brackets are not closed')
        return False, 'brackets are not closed'

def find_num(string):
    digits = list(map(str, list(range(0, 10))))
    num = ''
    i = 0
    char = string[i]
    while char in digits or char == '.':
        num += char
        i += 1
        if i < len(string):
            char = string[i]
        else:
            break
    try:
        return int(num)
    except:
        return float(num)

def calc(string):
    string = string.replace(" ",'')
    ans = None
    num = None
    digits = list(map(str,list(range(0,10))))
    i = 0
    # first deal with the brackets
    print('string:',string)
    i = 0
    char = string[i]
    # if I'll use 'for' the i+=1 won't work as expected
    while i < len(string):
        char = string[i]
        if char == 'A':
            ans = calc(string[i+1:])
            string = string[:i] + str(ans)
        if char == 'Z':
            return str(calc(string[:i])) + string[i+1:]
        i += 1
    print('string after bracket:',string)
    #################
    # now mul and div
    i = 0
    while i < len(string):
        char = string[i]
        if char in digits:
            num = find_num(string[i:])
            i += len(str(num))
            continue
        if num is None and char == '-':
            num = - (find_num(string[i+1:]))
            i += len(str(num))
            continue
        if char == '*' or char == '/':
            op = char
            i += 1
            char = string[i]
            # could be a number a bracket or a minus sign
            minus = False
            if char == '-':
                minus = True
                i += 1
                char = string[i]
            if char in digits:
                num2 = find_num(string[i:])
                if minus:
                    num2 = -num2
                    i -= 1
                i += len(str(num2))
                if op == '*':
                    ans = num * num2
                if op == '/':
                    ans = num / num2
                if ans % 1 == 0:
                    ans = int(ans)
                else:
                    ans = round(ans,2)
                k = i - (len(str(num)) + len(str(num2)) + 1)
                string = string[:k] + str(ans) + string[i:]
                i = k + len(str(ans))
                num = ans
            continue
        i += 1
    #################
    # now add and sub
    num = None
    ans = None
    i = 0
    while i < len(string):
        char = string[i]
        if char in digits:
            num = find_num(string[i:])
            i += len(str(num))
            continue
        if num is None and char == '-':
            num = - (find_num(string[i+1:]))
            i += len(str(num))
            continue
        if char == '+' or char == '-':
            op = char
            i += 1
            char = string[i]
            # could be a number a bracket or a minus sign
            minus = False
            if char == '-':
                minus = True
                i += 1
                char = string[i]
            if char in digits:
                num2 = find_num(string[i:])
                if minus:
                    num2 = -num2
                    i -= 1
                i += len(str(num2))
                if op == '+':
                    ans = num + num2
                if op == '-':
                    ans = num - num2
                k = i - (len(str(num)) + len(str(num2)) + 1)
                string = string[:k] + str(ans) + string[i:]
                i = k + len(str(ans))
                num = ans
            continue
        i += 1
    print('returning',ans)
    if ans is None:
        if not num is None:
            return num
        else:
            return 0
    return ans

print('Hi\n')

if __name__ == '__main__':
    string = '7*2+A7+3*A5-2ZZ/4*2'
    synOk, msg = syntaxOkay(string)
    if not synOk:
        print(msg)
        print('closing app')
        exit(0)
    print('syntax seems fine')
    print('begining calculation...\n')
    print(calc(string))


