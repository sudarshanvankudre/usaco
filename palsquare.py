"""
ID: sudarsh11
LANG: PYTHON3
TASK: palsquare
"""
mapping = {i: str(i) for i in range(10)}
mapping.update({10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'})

def is_palindrome(num):
    """
    >>> is_palindrome(2332)
    True
    >>> is_palindrome(1)
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(12344)
    False
    >>> is_palindrome(11211)
    True
    """
    num = str(num)
    if len(num) % 2 == 0:
        return num[:len(num) // 2] == num[len(num) // 2:][::-1]
    else:
        return num[:len(num) // 2] == num[len(num) // 2 + 1:][::-1]
        
def convert(num, B):
    """Returns num (given in base 10) in base B. num must be of type int
    >>> convert(255, 16)
    'FF'
    >>> convert(225, 16)
    'E1'
    >>> convert(6, 2)
    '110'
    """
    num = int(num)
    if num < B:
        return mapping[num]
    powers = []
    div, mod = divmod(num, B)
    while div > 0:
        powers.append(mod)
        div, mod = divmod(div, B)
    powers.append(mod)
    retval = ""
    while len(powers) > 0:
        retval += mapping[powers.pop()]
    return retval
    
with open("palsquare.in", "r") as fin:
    B = int(fin.readline())
with open("palsquare.out", "w") as fout:
    for n in range(1, 301):
        squared_based = convert(n ** 2, B)
        if is_palindrome(squared_based):
            based = convert(n, B)
            fout.write("{} {}\n".format(based, squared_based))
        
   
        
    
    