def number_to_word(n):
    if n == 0:
        return ''
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif n == 30:
        return 'thirty'
    elif n == 40:
        return 'forty'
    elif n == 50:
        return 'fifty'
    elif n == 60:
        return 'sixty'
    elif n == 70:
        return 'seventy'
    elif n == 80:
        return 'eighty'
    elif n == 90:
        return 'ninety'
    elif n >= 21 and n <= 99:
        return '%s-%s' % (number_to_word(n - n % 10),
                          number_to_word(n % 10))
    elif n >= 100 and n <= 999:
        if n % 100 == 0:
            return '%s hundred' % number_to_word(n / 100)
        else:
            return '%s hundred and %s' % (number_to_word(n / 100),
                                          number_to_word(n % 100))
    elif n == 1000:
        return 'one thousand'
    else:
        assert False


def letters(word):
    return len(word.replace('-', ' ').replace(' ', ''))


assert number_to_word(342) == 'three hundred and forty-two'
assert number_to_word(115) == 'one hundred and fifteen'

assert letters('three hundred and forty-two') == 23
assert letters('one hundred and fifteen') == 20


total = 0
for i in range(1, 1001):
    total += letters(number_to_word(i))
print total
