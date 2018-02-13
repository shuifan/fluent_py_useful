import contextlib


@contextlib.contextmanager
def reverse_print():
    import sys
    origin_print = sys.stdout.write

    def mirror(text):
        origin_print(text[::-1])
    sys.stdout.write = mirror
    try:
        yield 'abcd'
    finally:
        sys.stdout.write = origin_print


if __name__ == '__main__':

    with reverse_print() as text:
        print('How are you!')
        print(text)

    print('How are you!')
    print('Now is normal.')