import sys

def add(input):
    print(int(input) + 1)

def sub(input):
    print(int(input) - 1)

# function chooser
func_arg = {'-a': add, '-s': sub}

if __name__ == '__main__':
    try:
        func_arg[sys.argv[1]](sys.argv[2])
    except:
        print('enter func and input arg')

