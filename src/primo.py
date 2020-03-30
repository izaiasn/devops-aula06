print('-=' * 30)
print('= Os 100 Números Primos                                    =')
print('-=' * 30)
co = 0
for r in range(2, 548):
    c = 0
    for v in range(1, r+1):
        if r % v == 0:
            c += 1
    if c <= 2:
        print(r, end=' > ')
        co = co + 1
print('=-' * 25)
print('Essa é a contagem dos {} primeiros Primos'.format(co - 1))
print('=-' * 26)
