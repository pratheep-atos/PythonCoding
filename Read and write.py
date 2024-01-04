with open('venv/base.txt', 'r') as abc:
    content = abc.readlines()

    with open('venv/base.txt', 'w') as writer:
        for wr in reversed(content):
            writer.write(wr)

files = open('venv/base.txt')
str = files.read()
print(str)