from load_data import *


def parse_seq(s):
    # if first character is paren
    if len(s) == 0:
        return ''
    elif s[0] == '(':
        # then it's what we want, so let's parse it
        # -> get separator
        sep = s.index('x')
        # -> and closing paren
        end = s.index(')')
        # so that we can parse the length of the string to repeat
        length = int(s[1:sep])
        # and the number of times it is to be repeated
        times = int(s[(sep + 1):end])
        # fetch the string of length "length"
        repstr = s[(end + 1):(end + 1 + length)]
        # and repeat it "times" times
        repeatedstr = repstr*times
        # return this repeated string concatenated
        # with the rest of the parsed string
        return repeatedstr + parse_seq(s[end+1+length:])
    # if the first character is not a paren
    else:
        # then try the following
        try:
            # search for the next paren
            start = s.index('(')
            # and return the untouched part concatenated
            # with a substring whose first character is a paren
            return s[:start] + parse_seq(s[start:])
        # this could fail if there are no more parens left
        except ValueError as ve:
            # in this case, let's hope that we reached the end
            print('reached end of string??')
            print(ve)
            # if we have, then we should just return the last bit of the
            # string; it does not need to be parsed.
            return s


def parse_seq2(s):
    # if first character is paren
    if len(s) == 0:
        return 0
    elif s[0] == '(':
        # then it's what we want, so let's parse it
        # -> get separator
        sep = s.index('x')
        # -> and closing paren
        end = s.index(')')
        # so that we can parse the length of the string to repeat
        length = int(s[1:sep])
        # and the number of times it is to be repeated
        times = int(s[(sep + 1):end])
        # fetch the string of length "length"
        repstr = s[(end + 1):(end + 1 + length)]
        # and repeat it "times" times
        return times*parse_seq2(repstr) + parse_seq2(s[end+1+length:])
    # if the first character is not a paren
    else:
        # then try the following
        try:
            # search for the next paren
            start = s.index('(')
            # and return the untouched part concatenated
            # with a substring whose first character is a paren
            return len(s[:start]) + parse_seq2(s[start:])
        # this could fail if there are no more parens left
        except ValueError as ve:
            # in this case, let's hope that we reached the end
            # print('reached end of string??')
            # print(ve)
            # if we have, then we should just return the last bit of the
            # string; it does not need to be parsed.
            return len(s)


if __name__ == "__main__":

    tests = ['ADVENT', 'A(1x5)BC', '(3x3)XYZ', '(6x1)(1x3)A',
             'X(8x2)(3x3)ABCY']
    for t in tests:
        parsed_t = parse_seq(t)
        print(t)
        print(parsed_t)
        print()

    with open('./input/day9input.csv', 'r') as fp:
        data = fp.read()

    data = data[:-1]  # get rid of newline char
    parsed_data = parse_seq(data)
    print('Length of parsed data:')
    print(len(parsed_data))
    parsed2_data_length = parse_seq2(data)
    print('Length of parsed2 data')
    print(parsed2_data_length)


# Past guesses:
# * 150915
