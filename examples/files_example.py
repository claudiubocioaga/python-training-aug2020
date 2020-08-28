f = open('try_example.py')
for line in f:
    print(line, end='')
f.close()


with open('try_example.py') as f:
    for line in f:
        print(line, end='')


with open('out.txt', 'w+', encoding='utf-8') as f:
    print(f.tell())
    for line in f:
        pass
    print(f.tell())
    for nr in range(10, 15):
        f.write(f'{nr}. Test file write\n')
    print(f.tell())


with open('out_binary.txt', 'w+b') as f:
    print(f.tell())
    for nr in range(10, 15):
        f.write(b'Binary file\n')

    print(f.tell())
    f.seek(0)
    for line in f:
        print(line)

    f.seek(-10, 2)
    print(f.tell())
    print(f.read())
    print(f.tell())
