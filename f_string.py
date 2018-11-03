name = 'Wombat'
age = 69

print(f'Hello, {name}. You are of {age} years.', '\n')

# evaluated properly
print(f'{2 * 37}', '\n')

# call functions
def to_lower(input):
    return input.lower()

print(f'He is a {to_lower(name)}', '\n')

#direct call
print(f'I am a {name.lower()}', '\n')

# Can even be used with strings provided __str__() and __repr__() methods
# are defined.

# f-strings use str by default, but use repr with '!r' flag
## f'{class_instance!r}'

# multi-line, needs f in front of each line
message = (
    f'Hello.'
    f'Goodbye.'
)
print(message, '\n')

# using quotation marks
print(f"{'Eric Idle'}", '\n')

# with dictionaries
comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.", '\n')








