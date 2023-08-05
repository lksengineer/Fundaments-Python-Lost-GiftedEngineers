def anidado_uno():
    for row in range(1, 12):
        a = ''
        for x in range(1, row):
            a = a + 'x'
        print(a)


def anidado_dos():
    for row in range(1, 12):
        a = 12 - row
        toPrint = ''
        for _ in range(1, a):
            toPrint = toPrint + 'x'
        print(toPrint)


def run():
    anidado_uno()
    print('=='*8)
    anidado_dos()


if __name__ == '__main__':
    run()