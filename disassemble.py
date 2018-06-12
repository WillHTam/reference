import dis
def addup(L):
    sum = 0
    for i in L:
        sum += i
    return sum

def addp(L):
    sum = 0
    for i in L:
        sum = sum + i
    return sum

def func_obj(f):
    print('function name: ' + f.__name__)
    print('  co_varnames:',f.__code__.co_varnames)
    print('  co_names   :',f.__code__.co_names)
    print('  co_consts  :',f.__code__.co_consts,'\n')
    print('Source Line  m  operation/byte-code      operand (useful name/number)\n'+69*'-')
    dis.dis(f)

func_obj(addup)
print('\n')
func_obj(addp)
