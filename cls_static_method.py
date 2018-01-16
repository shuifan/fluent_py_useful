

class Demo:

    @classmethod
    def cls_method(*args):
        return args

    @staticmethod
    def static_method(*args):
        return args


if __name__ == '__main__':
    a = Demo.cls_method()
    print(a)
    b = Demo.static_method()
    print(b)