def make_average():
    history = []

    def average(new_value):
        history.append(new_value)
        total = sum(history)
        return total / len(history)

    return average


def make_average1():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return average

if __name__ == '__main__':
    a = make_average()
    b = make_average1()

    print(a(10))
    print(a(11))
    print(b(10))
    print(b(11))