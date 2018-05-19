def uppercase(f):
    def wrapper(): # define closure to wrap input function
        # wrapper closure has access to the function 
        # during, before, and after calling the input function
        original_result = f()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hellou!'

if __name__ == '__main__':
    print(greet())
