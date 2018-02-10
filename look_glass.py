import contextlib

class LookGlass:

    def __enter__(self):
        import sys
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'Fine, thank you!'

    def reverse_write(self, text):
        return self.origin_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.origin_write
        if exc_type is ZeroDivisionError:
            print('Please do not divide Zero!')
            return True


@contextlib.contextmanager
def look_glass():
    import sys
    origin_write = sys.stdout.write

    def reverse_write(text):
        return origin_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'How are you!'
    except BaseException:
        pass
    finally:
        sys.stdout.write = origin_write

if __name__ == '__main__':
    with look_glass() as text:
        print('How are you!')
        print(1/0)


    print(text)
    print('Back to normal!')