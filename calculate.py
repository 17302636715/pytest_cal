class Calculate(object):

    def add (self, a, b):
        return a + b

    def div(self, a, b):
        return a / b


if __name__ == '__main__':
    cal = Calculate()
    print(cal.add(1 + 2j, 2 + 3j))


