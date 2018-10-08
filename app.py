import re

print('Smart Python Calculator\n')
print('Allowed operations:')
print('   <equation>: evaluate <equation>')
print(' + <equation>: add')
print(' - <equation>: subtract')
print(' * <equation>: multiply')
print(' / <equation>: divide')
print(' % <equation>: modulo')
print('** <equation>: power')
print('         quit: exit\n')
print('Enter operation below and press <Enter> to evaluate')

ans = 0.0
run = True

def do_math():
    global run
    global ans

    try:
        eq = input(str(ans) + '\n')
        if eq == 'quit':
            run = False
            print('\nGoodbye human!')
        else:
            eq = re.sub('[a-zA-ZñÑ,;:_~^`´¨\'¡¿?=&$#"!|°¬@<>{}\[\] ]', '', eq)
            if re.search('(^0*\*\*0|[+-/*]0\*\*0)', eq):
                print('\033[31mERROR: cannot evaluate zero to the power of zero (0**0)\033[0m')
            else:
                if '.' in str(ans):
                    pf = '{:.' + str(2 ** len(str(ans).split('.')[1])) + 'f}'
                elif 'e' in str(ans):
                    pf = '{:.' + str(2 * abs(int(str(ans).split('e')[1]))) + 'f}'
                else:
                    pf = '{:.1f}'

                if eq.startswith('+') or eq.startswith('-') or eq.startswith('*') or eq.startswith('/'):
                    ans = float(pf.format(eval(str(ans) + eq)).rstrip('0').rstrip('.'))
                else:
                    ans = float(pf.format(eval(eq)).rstrip('0').rstrip('.'))

    except OverflowError as err:
        print('\033[31mERROR:', + err.args[1], '\033[0m')
    except ZeroDivisionError as err:
        print('\033[31mERROR:', err, '\033[0m')
    except SyntaxError:
        print('\033[31mERROR: invalid syntax\033[0m')
    except:
        raise


while run:
    do_math()