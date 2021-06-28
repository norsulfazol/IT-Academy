def get_value_or_default(t):
    def get_value(l, i):

        assert i > 0, "index should be greater then zero"

        if l is None:
            raise Exception

        try:
            return l[i]
        except IndexError:
            return t

    return get_value