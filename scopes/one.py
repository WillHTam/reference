import sys

def func():
    print("func() in one.py")

def functwo():
    answer = input('You are about to run this by itself. y/n?')
    if answer == 'y':
        func()
    elif answer == 'n':
        print('function call cancelled')
    else:
        print(globals()[sys.argv[1]])

print("top-level in one.py")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
    # print( globals() )
else:
    print('imported one')