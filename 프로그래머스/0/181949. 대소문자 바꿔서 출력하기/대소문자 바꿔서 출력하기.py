str = input()
for c in str:
    if c.isupper():
        print(c.lower(), end="")
    if c.islower():
        print(c.upper(), end="")