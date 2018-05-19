def strong(f):
    def wrap():
        return '<strong>' + f() + '</strong>'
    return wrap

def emphasis(f):
    def wrap():
        return '<em>' + f() + '</em>'
    return wrap

@strong
@emphasis
def greet():
    return 'hellou!'
# prints with strong as the outer tag
# => decorators applied from bottom to top

if __name__ == '__main__':
    print(greet())
