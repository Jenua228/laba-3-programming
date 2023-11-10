import re         #1)000000 2)00000-0000 3)XXXX 00

while True:
    index = input()
    match = re.search(r'\b\d{6}\b|\b\d{5}-\d{4}\b|\b([0-9]|[a-z]|[A-Z]){4} \d{2}\b', index)
    print('Right index' if match else 'Wrong index')