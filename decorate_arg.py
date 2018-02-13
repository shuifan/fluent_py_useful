registers = set()


def register(active=True):
    def decorate(func):
        print('Running register(active=%s) -> decorate(%s)'
              % (active, func))
        if active:
            registers.add(func)
        else:
            registers.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('f1 is running')
    a = 1
    b = 1
    print('fmt -> {a}'.format(**locals()))
    print(locals())


@register()
def f2():
    print('f2 is running ')


if __name__ == '__main__':
    print(registers)
    f1()


